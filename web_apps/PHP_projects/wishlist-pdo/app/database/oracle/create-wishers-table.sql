create table wishers (
    id number not null,
    name varchar2(50) unique not null,
    password varchar2(50) not null,
    constraint wishers_pk primary key(id)
);