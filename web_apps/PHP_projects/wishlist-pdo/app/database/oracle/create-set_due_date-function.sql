CREATE OR REPLACE
FUNCTION "SET_DUE_DATE" (in_date in VARCHAR2) return VARCHAR2 is
begin return TO_TIMESTAMP_TZ(in_date, 'YYYY-MM-DD HH24:MI:SS TZR');
end; /
