CREATE TABLE T_PLC_TAG_UNIT(
TAG_UNIT_ID NUMBER(2) NOT NULL,
TAG_UNIT_NAME VARCHAR2(25 BYTE) NOT NULL,
TAG_UNIT_DESC VARCHAR2(100 BYTE)
)

alter table T_PLC_TAG_UNIT add unique (TAG_UNIT_ID);