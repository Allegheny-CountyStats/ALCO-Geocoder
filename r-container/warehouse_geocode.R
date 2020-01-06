require(DBI)
require(dotenv)
require(rlang)

args <- commandArgs(trailingOnly=TRUE)

# Load Credentials
load_dot_env(".env")
un <- Sys.getenv("datawh_un")
pw <- Sys.getenv("datawh_pw")

# Load Geocoder functions
source("https://raw.githubusercontent.com/geoffreylarnold/ALCO-Geocoder/master/alco_geocoder.R")

# DB Connection String
con <- dbConnect(odbc::odbc(), driver = "{SQL Server Native Client 11.0}", server = "datawarehouse", UID = Un, pwd = pw, MARS_Connection = "Yes")

df <- dbReadTable(con, args[1]) %>% 
  mutate_countyGeo((!!rlang::sym(args[2])))

dbWriteTable(con, args[1], df)

dbDisconnect(con)