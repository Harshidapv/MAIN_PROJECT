/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 5.5.20-log : Database - costruction
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`costruction` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `costruction`;

/*Table structure for table `assign` */

DROP TABLE IF EXISTS `assign`;

CREATE TABLE `assign` (
  `aid` int(11) NOT NULL AUTO_INCREMENT,
  `rcid` int(11) NOT NULL,
  `wid` int(11) NOT NULL,
  `date` varchar(500) NOT NULL,
  `status` varchar(500) NOT NULL,
  PRIMARY KEY (`aid`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `assign` */

insert  into `assign`(`aid`,`rcid`,`wid`,`date`,`status`) values 
(1,1,6,'2023-04-30','completed'),
(2,1,6,'2023-05-05','completed'),
(3,1,6,'2023-05-05','completed'),
(4,1,6,'2023-05-05','Assigned');

/*Table structure for table `chat` */

DROP TABLE IF EXISTS `chat`;

CREATE TABLE `chat` (
  `chat_id` int(11) NOT NULL AUTO_INCREMENT,
  `from_id` int(11) NOT NULL,
  `to_id` int(11) NOT NULL,
  `chat` varchar(500) NOT NULL,
  `date` varchar(500) NOT NULL,
  `time` varchar(500) NOT NULL,
  PRIMARY KEY (`chat_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `chat` */

insert  into `chat`(`chat_id`,`from_id`,`to_id`,`chat`,`date`,`time`) values 
(1,2,4,'hello','2023-04-30','16:13:30'),
(2,4,4,'hi','2023-04-30','16:15:24'),
(3,4,2,'hi','2023-04-30','16:17:26'),
(4,4,2,'i have a plan','2023-05-05','11:02:41'),
(5,2,4,'tell me','2023-05-05','11:55:38');

/*Table structure for table `complaint` */

DROP TABLE IF EXISTS `complaint`;

CREATE TABLE `complaint` (
  `coid` int(11) NOT NULL AUTO_INCREMENT,
  `complaint` varchar(500) NOT NULL,
  `lid` int(11) NOT NULL,
  `date` varchar(500) NOT NULL,
  `reply` varchar(500) NOT NULL,
  PRIMARY KEY (`coid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `complaint` */

insert  into `complaint`(`coid`,`complaint`,`lid`,`date`,`reply`) values 
(1,'comp',2,'2023-04-30','ok'),
(2,'jbjbj',2,'2023-05-05','pending');

/*Table structure for table `contractor` */

DROP TABLE IF EXISTS `contractor`;

CREATE TABLE `contractor` (
  `cid` int(11) NOT NULL AUTO_INCREMENT,
  `lid` int(11) NOT NULL,
  `fname` varchar(500) NOT NULL,
  `lname` varchar(500) NOT NULL,
  `place` varchar(500) NOT NULL,
  `post` varchar(500) NOT NULL,
  `pin` varchar(500) NOT NULL,
  `email` varchar(500) NOT NULL,
  `phone` varchar(500) NOT NULL,
  `catogory` varchar(500) NOT NULL,
  PRIMARY KEY (`cid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `contractor` */

insert  into `contractor`(`cid`,`lid`,`fname`,`lname`,`place`,`post`,`pin`,`email`,`phone`,`catogory`) values 
(1,4,'Amal','kumar','kunnamkulam','kunnamkulam','673674','amal@gmail.com','9876504312','Industrial contractor');

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `fid` int(11) NOT NULL AUTO_INCREMENT,
  `cid` int(11) NOT NULL,
  `lid` int(11) NOT NULL,
  `feedback` varchar(500) NOT NULL,
  `date` varchar(500) NOT NULL,
  `emotion` varchar(500) NOT NULL,
  PRIMARY KEY (`fid`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

insert  into `feedback`(`fid`,`cid`,`lid`,`feedback`,`date`,`emotion`) values 
(1,4,2,'good','2023-04-30',''),
(2,4,2,'hv','2023-05-05',''),
(3,4,2,'good','2023-05-05','Positive');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `lid` int(10) NOT NULL AUTO_INCREMENT,
  `username` varchar(20) DEFAULT NULL,
  `password` varchar(20) DEFAULT NULL,
  `type` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`lid`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`lid`,`username`,`password`,`type`) values 
(1,'admin','Admin@123','admin'),
(2,'avinash','Avinash@123','user'),
(3,'madhav','Madhav@123','vendor'),
(4,'amal','Amal@123','contractor'),
(6,'kalindhi','Kalindhi@123','worker'),
(9,'harshi','harshi123@','user'),
(10,'paru','Paru123@','vendor');

/*Table structure for table `order` */

DROP TABLE IF EXISTS `order`;

CREATE TABLE `order` (
  `oid` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(11) DEFAULT NULL,
  `date` varchar(800) DEFAULT NULL,
  `amount` varchar(80) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`oid`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `order` */

insert  into `order`(`oid`,`uid`,`date`,`amount`,`status`) values 
(1,4,'2023-04-30','6400','Accepted'),
(2,4,'2023-05-05','171400','Accepted'),
(3,4,'2023-05-05','1000','ordered'),
(4,4,'2023-05-05','26800','cart');

/*Table structure for table `order_details` */

DROP TABLE IF EXISTS `order_details`;

CREATE TABLE `order_details` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `oid` int(11) DEFAULT NULL,
  `pid` int(11) DEFAULT NULL,
  `qty` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `order_details` */

insert  into `order_details`(`id`,`oid`,`pid`,`qty`) values 
(1,1,1,5),
(2,2,1,107),
(3,2,2,1),
(4,3,2,5),
(5,4,2,14),
(6,4,1,15);

/*Table structure for table `payment` */

DROP TABLE IF EXISTS `payment`;

CREATE TABLE `payment` (
  `payid` int(11) NOT NULL AUTO_INCREMENT,
  `oid` int(11) NOT NULL,
  `amount` float NOT NULL,
  `date` varchar(500) NOT NULL,
  PRIMARY KEY (`payid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `payment` */

insert  into `payment`(`payid`,`oid`,`amount`,`date`) values 
(1,4,6400,'2023-04-30'),
(2,4,6400,'2023-05-05');

/*Table structure for table `plan` */

DROP TABLE IF EXISTS `plan`;

CREATE TABLE `plan` (
  `pid` int(11) NOT NULL AUTO_INCREMENT,
  `cid` int(11) NOT NULL,
  `plan` varchar(500) NOT NULL,
  `details` varchar(500) NOT NULL,
  `image` varchar(500) NOT NULL,
  `date` varchar(500) NOT NULL,
  `req_id` varchar(500) NOT NULL,
  `status` varchar(500) NOT NULL,
  PRIMARY KEY (`pid`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `plan` */

insert  into `plan`(`pid`,`cid`,`plan`,`details`,`image`,`date`,`req_id`,`status`) values 
(1,4,' main plan','qwertyuiopasdfghjklzxcvbnm,','about.jpg','2023-04-30','1','Accepted');

/*Table structure for table `product` */

DROP TABLE IF EXISTS `product`;

CREATE TABLE `product` (
  `pid` int(11) NOT NULL AUTO_INCREMENT,
  `pname` varchar(500) NOT NULL,
  `image` varchar(500) NOT NULL,
  `price` int(11) NOT NULL,
  `vid` int(11) NOT NULL,
  PRIMARY KEY (`pid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `product` */

insert  into `product`(`pid`,`pname`,`image`,`price`,`vid`) values 
(1,'cement','services-3.jpg',1600,3),
(2,'cement','about.jpg',200,10);

/*Table structure for table `rating` */

DROP TABLE IF EXISTS `rating`;

CREATE TABLE `rating` (
  `rid` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(11) NOT NULL,
  `cid` int(11) NOT NULL,
  `rating` int(11) NOT NULL,
  `date` varchar(500) NOT NULL,
  PRIMARY KEY (`rid`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `rating` */

insert  into `rating`(`rid`,`uid`,`cid`,`rating`,`date`) values 
(1,2,4,4,'2023-04-30'),
(2,2,4,4,'2023-05-05'),
(3,2,4,3,'2023-05-05');

/*Table structure for table `request_for_contr` */

DROP TABLE IF EXISTS `request_for_contr`;

CREATE TABLE `request_for_contr` (
  `rcid` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(11) NOT NULL,
  `cid` int(11) NOT NULL,
  `work` varchar(500) NOT NULL,
  `details` varchar(500) NOT NULL,
  `date` varchar(500) NOT NULL,
  `status` varchar(500) NOT NULL,
  PRIMARY KEY (`rcid`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `request_for_contr` */

insert  into `request_for_contr`(`rcid`,`uid`,`cid`,`work`,`details`,`date`,`status`) values 
(1,2,4,'main office','full work','2023-04-30','Assigned'),
(2,2,4,'gfgg','jhghjg','2023-05-05','rejected'),
(3,2,4,'house','jhjh','2023-05-05','pending'),
(4,2,4,'building','yutyt','2023-05-05','pending');

/*Table structure for table `request_for_product` */

DROP TABLE IF EXISTS `request_for_product`;

CREATE TABLE `request_for_product` (
  `req_id` int(11) NOT NULL AUTO_INCREMENT,
  `pid` int(11) NOT NULL,
  `quantity` int(11) NOT NULL,
  `status` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`req_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `request_for_product` */

/*Table structure for table `salary` */

DROP TABLE IF EXISTS `salary`;

CREATE TABLE `salary` (
  `sid` int(11) NOT NULL AUTO_INCREMENT,
  `wid` int(11) NOT NULL,
  `salary` int(11) NOT NULL,
  `days` varchar(500) NOT NULL,
  PRIMARY KEY (`sid`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `salary` */

insert  into `salary`(`sid`,`wid`,`salary`,`days`) values 
(1,6,18400,'28'),
(3,0,50000,'45'),
(4,6,50000,'45');

/*Table structure for table `shedule` */

DROP TABLE IF EXISTS `shedule`;

CREATE TABLE `shedule` (
  `shed_id` int(11) NOT NULL AUTO_INCREMENT,
  `req_id` int(11) NOT NULL,
  `from date` varchar(500) NOT NULL,
  `to date` varchar(500) NOT NULL,
  `date` varchar(500) NOT NULL,
  `status` varchar(500) NOT NULL,
  PRIMARY KEY (`shed_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `shedule` */

insert  into `shedule`(`shed_id`,`req_id`,`from date`,`to date`,`date`,`status`) values 
(1,1,'2023-05-24','2023-05-31','2023-04-30','Reject'),
(3,1,'2023-05-05','2023-06-16','2023-05-05','Accepted'),
(4,1,'2023-05-05','2023-07-14','2023-05-05','Accepted');

/*Table structure for table `stock` */

DROP TABLE IF EXISTS `stock`;

CREATE TABLE `stock` (
  `stid` int(11) NOT NULL AUTO_INCREMENT,
  `pid` int(11) NOT NULL,
  `stock` int(11) NOT NULL,
  `date` varchar(500) NOT NULL,
  PRIMARY KEY (`stid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `stock` */

insert  into `stock`(`stid`,`pid`,`stock`,`date`) values 
(1,1,385,'2023-04-30'),
(2,2,380,'2023-05-05');

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `uid` int(11) NOT NULL AUTO_INCREMENT,
  `lid` int(11) NOT NULL,
  `fname` varchar(500) NOT NULL,
  `lname` varchar(500) NOT NULL,
  `place` varchar(500) NOT NULL,
  `post` varchar(500) NOT NULL,
  `pin` varchar(500) NOT NULL,
  `email` varchar(500) NOT NULL,
  `phone` bigint(11) NOT NULL,
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`uid`,`lid`,`fname`,`lname`,`place`,`post`,`pin`,`email`,`phone`) values 
(1,2,'Avinash','G','malapuram','malappuram','453627','avinash@123',8907563421),
(2,9,'Harshida','pv','Manjeri','kunnamkulam','679534','harshidapv2000@gmail.com',9645217256);

/*Table structure for table `vendor` */

DROP TABLE IF EXISTS `vendor`;

CREATE TABLE `vendor` (
  `vid` int(11) NOT NULL AUTO_INCREMENT,
  `lid` int(11) NOT NULL,
  `fname` varchar(500) NOT NULL,
  `lname` varchar(500) NOT NULL,
  `place` varchar(500) NOT NULL,
  `post` varchar(500) NOT NULL,
  `pin` varchar(500) NOT NULL,
  `email` varchar(500) NOT NULL,
  `phone` bigint(11) NOT NULL,
  PRIMARY KEY (`vid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `vendor` */

insert  into `vendor`(`vid`,`lid`,`fname`,`lname`,`place`,`post`,`pin`,`email`,`phone`) values 
(1,3,'madhav','gopinath','kozhikod','kozhikod','674532','madhav@gmail.com',8970564321),
(2,10,'parvathi','pp','Thrivandrum','Thiruvananthapuram','673674','parvathi@gmail.com',7856431287);

/*Table structure for table `work_amound` */

DROP TABLE IF EXISTS `work_amound`;

CREATE TABLE `work_amound` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `work_id` int(11) DEFAULT NULL,
  `amount` varchar(500) DEFAULT NULL,
  `date` varchar(500) DEFAULT NULL,
  `status` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `work_amound` */

insert  into `work_amound`(`id`,`work_id`,`amount`,`date`,`status`) values 
(1,1,'19000','2023-04-30','pending'),
(2,1,'60000','2023-05-05','pending'),
(3,1,'60000','2023-05-05','pending');

/*Table structure for table `worker` */

DROP TABLE IF EXISTS `worker`;

CREATE TABLE `worker` (
  `wid` int(11) NOT NULL AUTO_INCREMENT,
  `lid` int(11) NOT NULL,
  `cid` int(11) NOT NULL,
  `fname` varchar(500) NOT NULL,
  `lname` varchar(500) NOT NULL,
  `place` varchar(500) NOT NULL,
  `post` varchar(500) NOT NULL,
  `pin` varchar(500) NOT NULL,
  `phone` varchar(500) NOT NULL,
  `email` varchar(500) NOT NULL,
  PRIMARY KEY (`wid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `worker` */

insert  into `worker`(`wid`,`lid`,`cid`,`fname`,`lname`,`place`,`post`,`pin`,`phone`,`email`) values 
(1,6,4,'Kalindhi','krishnaa','Thalasseri','Thalasseri','673674','9087654123','kalindhi@gmail.com');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
