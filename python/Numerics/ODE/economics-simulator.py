
'''
  Initial Algorithm:
    Have N people
    Each person generates one of M resources, in quantity R_GEN per unit time
    Each person depletes R_CONSUME units of reserve in 1 unit of time
    Each person starts with R_START units of reserve
    Each person replenishes R_CONVERT units of reserve, by consuming 1 of each M resources

  Trading:
    [] v1: Infinite-Hunter-Gatherer: Exchange by first talking to everyone and guessing supply
    [] v2: Proportional-Communism:
       1) First pile all product in the same giant pile
       2) Then each person declares relative proportions of each product they need
       3) Then they take from pile computing a function of the amount they produced, and interests of everyone

  Extensions:
    [] Implement necessary/voluntary resources. All people need necessary, and a random subset of voluntary
    [] Implement distribution of production efficiency among people
    [] Implement finite storage capacity for reserve
    [] Implement large pulsed payments with large delay for some resources (i.e. Housing, Vehicles)


'''