import logging
import logstash
import socket

p_logger = logging.getLogger('python-logstash-logger')
p_logger.setLevel(logging.INFO)
p_logger.addHandler( logstash.LogstashHandler('3.86.213.48', 5959, version=1) )
p_logger.addHandler( logstash.TCPLogstashHandler('3.86.213.48', 5010, version=1) )


class Person(object):
    def __init__(self, personid, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.personid = personid
        p_logger.info("New Person Created: {} {}".format(firstname, lastname))

for i in range(7):
        p = Person(i, "John", "Doe")

p_logger.error('Python-Logstash: Logger working as expected')
p_logger.warning('New People Created!')
