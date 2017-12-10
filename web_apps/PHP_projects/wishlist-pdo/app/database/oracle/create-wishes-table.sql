create table wishes (
    id number not null,
    wisher_id number not null,
    description varchar2(255) not null,
    due_date TIMESTAMP (6) WITH TIME ZONE,
    constraint wishes_pk primary key(id),
    constraint wishes_fk1 foreign key(wisher_id) references wishers(id)
);