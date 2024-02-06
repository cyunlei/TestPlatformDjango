package com.zhouyu.service;

import com.zhouyu.mapper.UserMapper;
import org.springframework.beans.factory.annotation.Autowired;

public class UserService {

    @Autowired
    private UserMapper userMapper;

    public void test(){
        userMapper.insertOne();
        throw new NullPointerException();
    }
}
