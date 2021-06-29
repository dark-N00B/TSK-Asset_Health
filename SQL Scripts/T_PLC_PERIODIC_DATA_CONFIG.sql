CREATE TABLE T_PLC_PERIODIC_DATA_CONFIG(
ID_PLC_DATA_SEQ NUMBER(6) NOT NULL,
DATA_GENERATION_MODE VARCHAR2(5 BYTE),
COMPRESSION_UNITS VARCHAR2(1 BYTE),
TAG_UNIT_ID NUMBER(2) REFERENCES  T_PLC_TAG_UNIT(TAG_UNIT_ID),
COMPRESSION_ID NUMBER(2)  REFERENCES T_PLC_COMPRESSION_INFO(COMPRESSION_ID),
LCL NUMBER(12,4),
UCL NUMBER(12,4),
LSL NUMBER(12,4),
USL NUMBER(12,4)
);