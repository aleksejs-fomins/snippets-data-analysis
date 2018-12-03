import jpype
import numpy as np
import os
from sys import exit

JIDT_SHORTHAND_DICT = {
   "TE_DISCRETE"     : "infodynamics.measures.discrete.TransferEntropyCalculatorDiscrete",
   "TE_KERNEL"       : "infodynamics.measures.continuous.kernel.TransferEntropyCalculatorKernel",
   "TE_KRASKOV"      : "infodynamics.measures.continuous.kraskov.TransferEntropyCalculatorKraskov",
   "MI_MV_KRASKOV"   : "infodynamics.measures.continuous.kraskov.MutualInfoCalculatorMultiVariateKraskov1",
   "MI_MV_KERNEL"    : "infodynamics.measures.continuous.kernel.MutualInfoCalculatorMultiVariateKernel",
   "MI_MV_Gaussian"  : "infodynamics.measures.continuous.gaussian.MutualInfoCalculatorMultiVariateGaussian"
}

def np2JType(dataType):
   if 'int' in str(dataType):
      return jpype.JInt
   elif 'float' in str(dataType):
      return jpype.JDouble
   else:
      raise ValueError("Don't know how to convert data type", dataType, "to java")

def np2JArr(xarr):
   if type(xarr) is int:
      return xarr  # providing a single integer - apparently java can handle it without conversion
   elif type(xarr) is np.ndarray:
      jDim = 1 if len(xarr.shape) == 1 else xarr.shape[0]
      jType = np2JType(xarr.dtype)
      return jpype.JArray(jType, jDim)(xarr.tolist())
   elif 'jarray' in str(type(xarr)):
      return xarr  # data already in jarray format
   else:
      raise ValueError("Unexpected input data type ", type(xarr))


class JidtWrapper():
   def __init__(self, historyLength=2, kernelWidth=1):
       # Change location of jar to match yours (we assume script is called from demos/python):
       jarLocation = os.path.join(os.getcwd(), "jidt/infodynamics.jar");
       if (not (os.path.isfile(jarLocation))):
          exit("infodynamics.jar not found (expected at " + os.path.abspath(jarLocation) + ") - are you running from demos/python?")

       # Start the JVM (add the "-Xmx" option with say 1024M if you get crashes due to not enough memory space)
       jpype.startJVM(jpype.getDefaultJVMPath(), "-ea", "-Djava.class.path=" + jarLocation)

       # Extract signatures of various java classes from the package
       self.TECalcClassDiscrete = jpype.JPackage("infodynamics.measures.discrete").TransferEntropyCalculatorDiscrete
       self.MatrixUtils = jpype.JPackage('infodynamics.utils').MatrixUtils


   # Constructor - Run when with statement is entered
   def __enter__(self):
       return self


   # Destructor - Run when with statement is exited
   def __exit__(self, exc_type, exc_value, traceback):
       jpype.shutdownJVM()


   # Extract method class
   def getJavaClass(self, classShorthand):
      if classShorthand in JIDT_SHORTHAND_DICT.keys():
         classRef = JIDT_SHORTHAND_DICT[classShorthand]
         indexOfLastDot = classRef.rfind(".")
         classType = eval('jpype.JPackage("' + classRef[:indexOfLastDot] + '").' + classRef[indexOfLastDot + 1:])
         return classType
      else:
         raise ValueError("Unknown method", classShorthand)


   def runJavaTwoPartite(self, data, param):
        self.javaClass = self.getJavaClass(param["method"])()
        self.javaClass.initialise(*param['initParam'])
        for key, value in param['properties'].items():
            self.javaClass.setProperty(key, value)

        if ('CONTINUOUS_DATA' in param.keys()) and (param['CONTINUOUS_DATA'] == True):
            self.javaClass.startAddObservations()
            return self.javaClass
        elif ('NO_CONV_JARRAY' in param.keys()) and (param['NO_CONV_JARRAY'] == True):
            self.javaClass.setObservations(data[0], data[1])
            return self.javaClass.computeAverageLocalOfObservations()
        else:
            self.javaClass.setObservations(np2JArr(data[0]), np2JArr(data[1]))
            return self.javaClass.computeAverageLocalOfObservations()


   def calcTwoPartiteTE_Discrete(self, xarr, yarr, param):
       self.javaClass = self.TECalcClassDiscrete(param['historyLength'], param['kernelWidth'])
       self.javaClass.initialise()
       self.javaClass.addObservations(np2JArr(xarr), np2JArr(yarr))
       return self.javaClass.computeAverageLocalOfObservations()


   # TODO: Why all of a sudden we are column-major???
   def computeCombinedValues(self, mat):
      return self.MatrixUtils.computeCombinedValues(mat.tolist(), mat.shape[1])