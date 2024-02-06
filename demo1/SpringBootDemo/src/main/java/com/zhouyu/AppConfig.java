package com.zhouyu;


import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.PropertySource;

@Configuration
@ComponentScan
@MapperScan
@PropertySource()
public class AppConfig {

}
