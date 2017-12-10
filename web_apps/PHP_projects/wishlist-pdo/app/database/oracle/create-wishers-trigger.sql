create or replace trigger wishers_insert
before insert on wishers
for each row
begin
    select wishers_id_seq.nextval into :new.id from dual;
end;
/