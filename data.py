
import kagglehub
from kagglehub import KaggleDatasetAdapter

file_path = "clean_sql_dataset.csv"

# Load the latest version
lf = kagglehub.load_dataset(
  KaggleDatasetAdapter.POLARS,
  "gambleryu/biggest-sql-injection-dataset",
  file_path,
 
)

print("First 5 records:", lf.collect().head())
