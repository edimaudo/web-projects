create or replace trigger wishes_insert
before insert on wishes
for each row
begin
    select wishes_id_seq.nextval into :new.id from dual;
end;
/