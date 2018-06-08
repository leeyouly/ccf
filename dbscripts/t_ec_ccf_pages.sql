create table t_ec_ccf_pages
(
   url varchar2(500) not null constraint t_ec_ccf_pages_pk primary key,
   CREATE_DT DATE DEFAULT sysdate NOT NULL ENABLE
);