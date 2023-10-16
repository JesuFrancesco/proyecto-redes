# parece solo funcionar en linux, no se pq...............
import uuid
from pprint import pprint

# Import the required measurement.
import netmeasure.measurements.file_download.measurements as fdms

# se requiere instalar la librería youtube-dl

latencia = fdms.FileDownloadMeasurement(id=uuid.uuid4, urls=["https://github.com/ppy/osu/releases/latest/download/install.exe"])

# Run the measurement.
resultado = latencia.measure()

# Print the measurement result(s)
pprint(resultado)