# Module for Query Orginization

    # SQLITE DATA TYPES
    # NULL
    # INTEGER
    # REAL
    # TEXT
    # BLOB


# Create Tables

CREATE_TABLE_CLIENT = ("""CREATE TABLE IF NOT EXISTS client (
	ESIID INTEGER PRIMARY KEY ,
	lastUpdatedDate DATE NOT NULL
)WITHOUT ROWID;""")

CREATE_TABLE_ERCOT = ("""CREATE TABLE IF NOT EXISTS ERCOT (
	ERCOTDUNSNumber TEXT PRIMARY KEY,
	lastUpdatedDate DATE NOT NULL
)WITHOUT ROWID;""")

CREATE_TABLE_CR = ("""CREATE TABLE IF NOT EXISTS competitiveRetailer (
    CRDUNSNumber TEXT NOT NULL PRIMARY KEY,
    CRName TEXT NOT NULL,
    CRDUNSCode INTEGER NOT NULL,
	lastUpdatedDate DATE NOT NULL
);""")

CREATE_TABLE_TDSP = ("""CREATE TABLE IF NOT EXISTS TDSP (
    TDSPDUNSNumber TEXT NOT NULL PRIMARY KEY,
    TDSPName TEXT NOT NULL,
    TDSPDUNSCode INTEGER NOT NULL,
	lastUpdatedDate DATE NOT NULL
)WITHOUT ROWID;""")

CREATE_TABLE_TRANSACTIONS = ("""CREATE TABLE IF NOT EXISTS transactions (
    transactionID TEXT PRIMARY KEY,
    transactionCreationDate DATE NOT NULL,
    transactionSetPurposeCode INTEGER NOT NULL,
    ESIID INTEGER NOT NULL,
    CRDUNSNumber NULL,
    CREntityCode INTEGER NULL,
    TDSPDUNSNumber TEXT NULL,
    TDSPEntityCode NULL,
    ERCOTEntityCode INTEGER NULL,
    originatorReferenceID INTEGER NOT NULL,
    historicalReferenceID INTEGER NOT NULL,
    reportTypeCode TEXT NULL,
    lastUpdatedDate DATE NOT NULL,
    FOREIGN KEY(ESIID) REFERENCES client(ESIID),
    FOREIGN KEY(CRDUNSNumber) REFERENCES competitiveRetailer(CRDUNSNumber),
    FOREIGN KEY(TDSPDUNSNumber) REFERENCES TDSP(TDSPDUNSNumber)

)WITHOUT ROWID;""")

CREATE_TABLE_UNMETEREDSERVICE = """CREATE TABLE IF NOT EXISTS unmeteredService (
    transactionID TEXT NOT NULL,
    servicePeriodStart INTEGER NOT NULL,
    servicePeriodEnd INTEGER NOT NULL,
    serviceTypeReferenceID TEXT NOT NULL,
    description TEXT NULL,
    quantityQualifier TEXT NOT NULL,
    quantityValue INTEGER NOT NULL,
    unitCodeBase TEXT NOT NULL,
    numberOfDevicesMultiplier REAL,
    unitCode TEXT NOT NULL,
    consumptionPerDeviceMultiplier REAL,
    lastUpdatedDate DATE NOT NULL,
    PRIMARY KEY (transactionID, servicePeriodStart, servicePeriodEnd),
    FOREIGN KEY(transactionID) REFERENCES transactions(transactionID)

)WITHOUT ROWID;"""

CREATE_TABLE_NONINTERVALSERVICE = """CREATE TABLE IF NOT EXISTS nonIntervalService (
    transactionID TEXT NOT NULL,
    meterSerial TEXT,
    meterRoleID TEXT,
    meterTypeID TEXT,
    movementTypeCode TEXT,
    servicePeriodStart INTEGER NOT NULL,
    servicePeriodEnd INTEGER NOT NULL,
    exchangeDate TEXT,
    quantityQualifier TEXT NOT NULL,
    quantityValue TEXT NOT NULL,
    meterReadsValue TEXT NOT NULL,
    meterReadsSignificanceCode TEXT,
    transformerLossFactor TEXT,
    meterMultiplier TEXT,
    powerFactor TEXT,
    lastUpdatedDate DATE NOT NULL,
    PRIMARY KEY (transactionID, servicePeriodStart, servicePeriodEnd),
    FOREIGN KEY(transactionID) REFERENCES transactions(transactionID)

)WITHOUT ROWID;"""

CREATE_TABLE_INTERVALSERVICESUMMARY = """CREATE TABLE IF NOT EXISTS intervalServiceSummary (
    transactionID TEXT NOT NULL,
    meterSerial TEXT NOT NULL,
    meterRoleID TEXT,
    meterTypeID TEXT,
    movementTypeCode TEXT,
    servicePeriodStart INTEGER NOT NULL,
    servicePeriodEnd INTEGER NOT NULL,
    exchangeDate INTEGER NULL,
    quantityQualifier TEXT NOT NULL,
    quantityValue TEXT NOT NULL,
    transformerLossFactor TEXT,
    powerFactor TEXT,
    lastUpdatedDate DATE NOT NULL,
    PRIMARY KEY (transactionID, servicePeriodStart, servicePeriodEnd),
    FOREIGN KEY(transactionID) REFERENCES transactions(transactionID)

)WITHOUT ROWID;"""

CREATE_TABLE_INTERVALSERVICEDETAIL = """CREATE TABLE IF NOT EXISTS intervalServiceDetail (
    service_loop_uuid TEXT NOT NULL,
    transactionID TEXT NOT NULL,
    channelNumber TEXT,
    meterSerial TEXT,
    meterRoleID TEXT,
    meterTypeID TEXT,
    movementTypeCode TEXT,
    servicePeriodStart INTEGER NOT NULL,
    servicePeriodEnd INTEGER NOT NULL,
    exchangeDate TEXT,
    lastUpdatedDate DATE NOT NULL,
    PRIMARY KEY (channelNumber, servicePeriodStart, servicePeriodEnd),
    FOREIGN KEY(transactionID) REFERENCES transactions(transactionID)

)WITHOUT ROWID;"""

CREATE_TABLE_INTERVALSERVICELOOP = """CREATE TABLE IF NOT EXISTS intervalServiceLoop (
    service_loop_uuid TEXT NOT NULL,
    transactionID TEXT NOT NULL,
    channelNumber TEXT,
    quantityQualifier TEXT NOT NULL,
    quantityValue INTEGER NOT NULL,
    intervalEndDate INTEGER NOT NULL,
    intervalENDTime INTEGER NOT NULL,   
    lastUpdatedDate DATE NOT NULL, 
    PRIMARY KEY (channelNumber, intervalEndDate, intervalENDTime),
    FOREIGN KEY(transactionID) REFERENCES transactions(transactionID)
)WITHOUT ROWID;"""

# Table Tuple
DEFAULT_TABLES = (CREATE_TABLE_CLIENT, CREATE_TABLE_ERCOT, CREATE_TABLE_CR, CREATE_TABLE_TDSP, CREATE_TABLE_TRANSACTIONS, CREATE_TABLE_UNMETEREDSERVICE, CREATE_TABLE_NONINTERVALSERVICE, CREATE_TABLE_INTERVALSERVICESUMMARY, CREATE_TABLE_INTERVALSERVICEDETAIL, CREATE_TABLE_INTERVALSERVICELOOP)

# Insert Statements

INSERT_CLIENT = """INSERT or IGNORE INTO client(
    ESIID,
	lastUpdatedDate
)VALUES(?,?);"""

INSERT_ERCOT = """INSERT or IGNORE INTO ERCOT(
    ERCOTDUNSNumber,
    lastUpdatedDate
)VALUES(?,?);"""

INSERT_CR = """INSERT or IGNORE INTO competitiveRetailer(
	CRName,
    CRDUNSCode,
    CRDUNSNumber,
	lastUpdatedDate
)VALUES(?,?,?,?);"""

INSERT_TDSP = """INSERT OR IGNORE INTO TDSP(
    TDSPDUNSNumber,
    TDSPName,
    TDSPDUNSCode,
	lastUpdatedDate
)VALUES(?,?,?,?);"""

INSERT_TRANSACTIONS = """INSERT OR IGNORE INTO transactions(
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
    lastUpdatedDate
)VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?);"""

INSERT_UNMETEREDSERVICE = """INSERT OR IGNORE INTO unmeteredService(
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
    lastUpdatedDate
)VALUES(?,?,?,?,?,?,?,?,?,?,?,?);"""

INSERT_NONINTERVALSERVICE = """INSERT OR IGNORE INTO nonIntervalService(
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
    lastUpdatedDate
)VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);"""

INSERT_INTERVALSERVICESUMMARY = """INSERT OR IGNORE INTO intervalServiceSummary(
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
    lastUpdatedDate
)VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?);"""

INSERT_INTERVALSERVICEDETAIL = """INSERT OR IGNORE INTO intervalServiceDetail(
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
    lastUpdatedDate
)VALUES(?,?,?,?,?,?,?,?,?,?,?);"""


INSERT_INTERVALSERVICELOOP = """INSERT OR IGNORE INTO intervalServiceLoop(
    service_loop_uuid,
    transactionID,
    channelNumber,
    quantityQualifier,
    quantityValue,
    intervalEndDate,
    intervalENDTime,    
    lastUpdatedDate
)VALUES(?,?,?,?,?,?,?,?);"""