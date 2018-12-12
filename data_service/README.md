# Data Service

Data service stores information of all successful client requests.

Pre-requisites - Python3, Django and PostgreSQL

# Functionalities:
To get list of transaction :  localhost/transactionlist/

To get a particular transaction requested by particular client (sender) :  localhost/transactionlist/sender/pk1(sender_name)/txnid/pk2(transaction_id)/

To get all transactions requested by particular client (sender) : localhost/transactionlist/sender/pk1(sender_name)/

To get all the transactions received by particular client (receiver) :  localhost/transactionlist/receiver/pk(receiver_name)/

To get all the transactions requested for a particular client (receiver) :  localhost/transactionlist/sender/pk1(sender_name)/receiver/pk2(receiver_name)/
