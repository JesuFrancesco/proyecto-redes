# parece solo funcionar en linux por la carpeta nul...............
import uuid
from pprint import pprint

# Import the required measurement.
import netmeasure.measurements.youtube_download.measurements as ytms

# se requiere instalar la librería youtube-dl

latencia = ytms.YoutubeDownloadMeasurement(id=uuid.uuid4(), url="https://youtu.be/7RaGlYZCfnQ?si=3QerweH_BqZpqjYH")

# Run the measurement.
resultado = latencia.measure()

# Print the measurement result(s)
pprint(resultado)