#!/usr/bin/env Rscript

# Bhishan Poudel
# Jan 8, 2016

# clear; Rscript functions.r; rm *~


# Example of a Function
pow <- function(x, y) {
   # function to print x raised to the power y

   result <- x^y
   print(paste(x,"raised to the power",y,"is",result))
}


# Function Calls
pow(8,2)
pow(2,8)

# Named Arguments
pow(x=8, y=2)
pow(y=2, x=8)
pow(x=8, 2)

# Default Values for Arguments
pow <- function(x, y=2) {
   # function to print x raised to the power y
   result <- x^y
   print(paste(x,"raised to the power",y,"is",result))
}

# function call
pow(3)
# [1] "3 raised to the power 2 is 9"
pow(3,1)
# [1] "3 raised to the power 1 is 3"


# Returning an object
#By default the value of the last line is returned.
cat("\n\n")

test <- function(){
  x <-1
  y <- 2
  z <- 3
  #return(x)
  }
res <- test()
res
