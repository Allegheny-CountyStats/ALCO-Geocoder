FROM countystats/r-geo:1.0
ARG table
ARG column

MAINTAINER Geoffrey Arnold "geoffrey.arnold@alleghenycounty.us"

RUN Rscript warehouse_geocode.R $table $column