/** 创建用户表 */
const user =
  "CREATE TABLE if not EXISTS users(id int PRIMARY key auto_increment,account varchar(32),username varchar(32),password varchar(32),time DATETIME,details TEXT)";

export { user };
