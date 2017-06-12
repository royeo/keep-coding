const Sequelize = require('sequelize');

let sequelize = new Sequelize({
  host: 'localhost',
  port: 3306,
  dialect: 'mysql',
  
})