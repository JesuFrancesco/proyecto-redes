# ESTA SI ME DEJO EN WINDOWS
import uuid
from pprint import pprint

# Import the required measurement.
# from netmeasure.measurements.latency.measurements import LatencyMeasurement
import netmeasure.measurements.speedtest_dotnet.measurements as sptest

# en este caso usare la primera id del primer sv
latencia = sptest.SpeedtestDotnetMeasurement(id=uuid.uuid4(), servers=[3852])

# Run the measurement.
resultado = latencia.measure()

# Print the measurement result(s)
pprint(resultado)