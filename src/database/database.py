import sqlite3
import database.queries as queries

def connect():
    return sqlite3.connect('./src/database/octopus.db')

def create_tables(connection):
    with connection:
        for table in queries.DEFAULT_TABLES:
            connection.execute(table)
        return 'Tables Created'

def add_clients(connection, ESIID, lastUpdatedDate):
    with connection:
        connection.execute(queries.INSERT_CLIENT, (ESIID, lastUpdatedDate))

def add_ERCOT(connection, ERCOTDUNSNumber, lastUpdatedDate):
    with connection:
        connection.execute(queries.INSERT_ERCOT, (ERCOTDUNSNumber, lastUpdatedDate))

def add_CR(connection, CRName, CRDUNSCode, CRDUNSNumber, lastUpdatedDate):
    with connection:
        connection.execute(queries.INSERT_CR, (CRName, CRDUNSCode, CRDUNSNumber, lastUpdatedDate))

def add_TDSP(connection, TDSPDUNSNumber, TDSPName, TDSPDUNSCode, lastUpdatedDate):
    with connection:
        connection.execute(queries.INSERT_TDSP, (TDSPDUNSNumber, TDSPName, TDSPDUNSCode, lastUpdatedDate))

def add_transaction(
    connection,
    transactionID,
    transactionCreationDate,
    transactionSetPurposeCode,
    ESIID,
    CRDUNSNumber,
    CREntityCode,
    TDSPDUNSNumber,
    TDSPEntityCode,
    ERCOTEntityCode,
    originatorReferenceID,
    historicalReferenceID,
    reportTypeCode,
    lastUpdatedDate):
    with connection:
        connection.execute(queries.INSERT_TRANSACTIONS,(
            transactionID,
            transactionCreationDate,
            transactionSetPurposeCode,
            ESIID,
            CRDUNSNumber,
            CREntityCode,
            TDSPDUNSNumber,
            TDSPEntityCode,
            ERCOTEntityCode,
            originatorReferenceID,
            historicalReferenceID,
            reportTypeCode,
            lastUpdatedDate))

def add_unmeteredService(
    connection,
    transactionID,
    servicePeriodStart,
    servicePeriodEnd,
    serviceTypeReferenceID,
    description,
    quantityQualifier,
    quantityValue,
    unitCodeBase,
    numberOfDevicesMultiplier,
    unitCode,
    consumptionPerDeviceMultiplier,
    lastUpdatedDate):
    with connection:
        connection.execute(queries.INSERT_UNMETEREDSERVICE,(
            transactionID,
            servicePeriodStart,
            servicePeriodEnd,
            serviceTypeReferenceID,
            description,
            quantityQualifier,
            quantityValue,
            unitCodeBase,
            numberOfDevicesMultiplier,
            unitCode,
            consumptionPerDeviceMultiplier,
            lastUpdatedDate))


def add_nonIntervalService(
    connection,
    transactionID,
    meterSerial,
    meterRoleID,
    meterTypeID,
    movementTypeCode,
    servicePeriodStart,
    servicePeriodEnd,
    exchangeDate,
    quantityQualifier,
    quantityValue,
    meterReadsValue,
    meterReadsSignificanceCode,
    transformerLossFactor,
    meterMultiplier,
    powerFactor,
    lastUpdatedDate):
    with connection:
        connection.execute(queries.INSERT_NONINTERVALSERVICE,(
            transactionID,
            meterSerial,
            meterRoleID,
            meterTypeID,
            movementTypeCode,
            servicePeriodStart,
            servicePeriodEnd,
            exchangeDate,
            quantityQualifier,
            quantityValue,
            meterReadsValue,
            meterReadsSignificanceCode,
            transformerLossFactor,
            meterMultiplier,
            powerFactor,
            lastUpdatedDate))

def add_intervalServiceSummary(
    connection,
    transactionID,
    meterSerial,
    meterRoleID,
    meterTypeID,
    movementTypeCode,
    servicePeriodStart,
    servicePeriodEnd,
    exchangeDate,
    quantityQualifier,
    quantityValue,
    transformerLossFactor,
    powerFactor,
    lastUpdatedDate):
    with connection:
        connection.execute(queries.INSERT_INTERVALSERVICESUMMARY,(
            transactionID,
            meterSerial,
            meterRoleID,
            meterTypeID,
            movementTypeCode,
            servicePeriodStart,
            servicePeriodEnd,
            exchangeDate,
            quantityQualifier,
            quantityValue,
            transformerLossFactor,
            powerFactor,
            lastUpdatedDate))          

def add_intervalServiceDetail(
    connection,
    service_loop_uuid,
    transactionID,
    channelNumber,
    meterSerial,
    meterRoleID,
    meterTypeID,
    movementTypeCode,
    servicePeriodStart,
    servicePeriodEnd,
    exchangeDate,
    lastUpdatedDate):
    with connection:
        connection.execute(queries.INSERT_INTERVALSERVICEDETAIL,(
            service_loop_uuid,
            transactionID,
            channelNumber,
            meterSerial,
            meterRoleID,
            meterTypeID,
            movementTypeCode,
            servicePeriodStart,
            servicePeriodEnd,
            exchangeDate,
            lastUpdatedDate))     

def add_intervalServiceLoop(
    connection,
    service_loop_uuid,
    transactionID,
    channelNumber,
    quantityQualifier,
    quantityValue,
    intervalEndDate,
    intervalENDTime,       
    lastUpdatedDate):
    with connection:
        connection.execute(queries.INSERT_INTERVALSERVICELOOP,(
            service_loop_uuid,
            transactionID,
            channelNumber,
            quantityQualifier,
            quantityValue,
            intervalEndDate,
            intervalENDTime,     
            lastUpdatedDate)) 

if __name__ == '__main__':
    print('intended to use as MOD')

 