drop user phpuser cascade;
create user phpuser identified by phpuserpw;
grant connect, resource to phpuser;
alter user phpuser default tablespace users temporary tablespace temp account unlock;