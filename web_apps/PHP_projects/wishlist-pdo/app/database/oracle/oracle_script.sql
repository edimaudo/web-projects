CREATE TABLE "HTMLDB_PLAN_TABLE" (
    "STATEMENT_ID" VARCHAR2(30),
    "PLAN_ID" NUMBER,
    "TIMESTAMP" DATE,
    "REMARKS" VARCHAR2(4000),
    "OPERATION" VARCHAR2(30),
    "OPTIONS" VARCHAR2(255),
    "OBJECT_NODE" VARCHAR2(128),
    "OBJECT_OWNER" VARCHAR2(30),
    "OBJECT_NAME" VARCHAR2(30),
    "OBJECT_ALIAS" VARCHAR2(65),
    "OBJECT_INSTANCE" NUMBER(*,0),
    "OBJECT_TYPE" VARCHAR2(30),
    "OPTIMIZER" VARCHAR2(255),
    "SEARCH_COLUMNS" NUMBER,
    "ID" NUMBER(*,0),
    "PARENT_ID" NUMBER(*,0),
    "DEPTH" NUMBER(*,0),
    "POSITION" NUMBER(*,0),
    "COST" NUMBER(*,0),
    "CARDINALITY" NUMBER(*,0),
    "BYTES" NUMBER(*,0),
    "OTHER_TAG" VARCHAR2(255),
    "PARTITION_START" VARCHAR2(255),
    "PARTITION_STOP" VARCHAR2(255),
    "PARTITION_ID" NUMBER(*,0),
    "OTHER" LONG,
    "DISTRIBUTION" VARCHAR2(30),
    "CPU_COST" NUMBER(*,0),
    "IO_COST" NUMBER(*,0),
    "TEMP_SPACE" NUMBER(*,0),
    "ACCESS_PREDICATES" VARCHAR2(4000),
    "FILTER_PREDICATES" VARCHAR2(4000),
    "PROJECTION" VARCHAR2(4000),
    "TIME" NUMBER(*,0),
    "QBLOCK_NAME" VARCHAR2(30) ) /

CREATE TABLE "WISHERS" (
    "ID" NUMBER NOT NULL ENABLE,
    "NAME" VARCHAR2(50) NOT NULL ENABLE,
    "PASSWORD" VARCHAR2(50) NOT NULL ENABLE,
    CONSTRAINT "WISHERS_PK" PRIMARY KEY ("ID") ENABLE,
    UNIQUE ("NAME") ENABLE
) /

CREATE TABLE "WISHES" (
    "ID" NUMBER NOT NULL ENABLE,
    "WISHER_ID" NUMBER NOT NULL ENABLE,
    "DESCRIPTION" VARCHAR2(255) NOT NULL ENABLE,
    "DUE_DATE" TIMESTAMP (6) WITH TIME ZONE,
    CONSTRAINT "WISHES_PK" PRIMARY KEY ("ID") ENABLE,
    CONSTRAINT "WISHES_FK1" FOREIGN KEY ("WISHER_ID")
    REFERENCES "WISHERS" ("ID") ENABLE
) /

CREATE OR REPLACE
FUNCTION "SET_DUE_DATE" (in_date in VARCHAR2) return VARCHAR2 is
begin return TO_TIMESTAMP_TZ(in_date, 'YYYY-MM-DD HH24:MI:SS TZR');
end; /

CREATE OR REPLACE
FUNCTION "FORMAT_DUE_DATE" (in_date in TIMESTAMP) return VARCHAR2 is
begin
return TO_CHAR(IN_DATE, 'YYYY-MM-DD HH24:MI:SS TZR');
end; /

CREATE UNIQUE INDEX "WISHES_PK" ON "WISHES" ("ID") /
CREATE UNIQUE INDEX "WISHERS_PK" ON "WISHERS" ("ID") /
CREATE UNIQUE INDEX "SYS_C004149" ON "WISHERS" ("NAME") /
CREATE SEQUENCE "WISHES_ID_SEQ"
MINVALUE 1 MAXVALUE 999999999999999999999999999 INCREMENT BY 1
START WITH 30 CACHE 20 NOORDER NOCYCLE /

CREATE SEQUENCE "WISHERS_ID_SEQ"
MINVALUE 1 MAXVALUE 999999999999999999999999999 INCREMENT BY 1
START WITH 23 CACHE 20 NOORDER NOCYCLE /

CREATE OR REPLACE
TRIGGER "WISHES_INSERT" BEFORE insert on "WISHES" for each row
begin
select WISHES_ID_SEQ.NEXTVAL into :NEW.ID from dual;
end; /

ALTER TRIGGER "WISHES_INSERT" ENABLE /

CREATE OR REPLACE TRIGGER "WISHERS_INSERT" BEFORE insert on "WISHERS" for each row
begin
select WISHERS_ID_SEQ.NEXTVAL into :NEW.ID from dual;
end; /
ALTER TRIGGER "WISHERS_INSERT" ENABLE /