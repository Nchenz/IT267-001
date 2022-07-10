from abank import Abank

scb = Abank('SCB')
scb.loanamount = 100000
scb.loanrate = 3
scb.loanyear = 2
scb.display_interest()