drop table if exists logs;
create table logs(
        id integer primary key autoincrement,
        username text not null,
        movement text not null,
        weight numeric not null,
        repetitions numeric not null,
        rpe numeric not null
);
