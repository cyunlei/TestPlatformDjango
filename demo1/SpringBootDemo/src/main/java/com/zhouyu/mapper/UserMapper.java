package com.zhouyu.mapper;

public interface UserMapper {
    @Insert("insert into t1 values(1,1,1,1,1,'1')")
    void insertOne();
}
