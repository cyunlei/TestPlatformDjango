package com.zhouyu.springbootdemo1;

import org.hibernate.annotations.SQLInsert;

public interface UserName {

    @Insert("insert into")
    void InsertOne();
}
