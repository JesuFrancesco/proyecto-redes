# requiere scapy
# funca en linux
# parece pedir un permiso adicional
"""
 LatencyMeasurementResult(id=UUID('3941aa6b-91ac-4d69-b03c-d6d31d98ca30'),
                          errors=[Error(key='ping-err',
                                        description='ping had an unknown error',
                                        traceback='')],
                          host='190.117.114.206',
                          minimum_latency=None,
                          average_latency=None,
                          maximum_latency=None,
                          median_deviation=None,
                          packets_transmitted=None,
                          packets_received=None,
                          packets_lost=None,
                          packets_lost_unit=None,
                          elapsed_time=None,
                          elapsed_time_unit=None)]

"""
import uuid
from pprint import pprint

# Import the required measurement.
import netmeasure.measurements.ip_route.measurements as ipms

# en este caso usare la primera id del primer sv
latencia = ipms.IPRouteMeasurement(id=uuid.uuid4(), hosts=["8.8.8.8"])

# Run the measurement.
resultado = latencia.measure()

# Print the measurement result(s)
pprint(resultado)