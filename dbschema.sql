-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema appointmentspylotdb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema appointmentspylotdb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `appointmentspylotdb` DEFAULT CHARACTER SET utf8 ;
USE `appointmentspylotdb` ;

-- -----------------------------------------------------
-- Table `appointmentspylotdb`.`appointment`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `appointmentspylotdb`.`appointment` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `user_id` INT(11) NOT NULL,
  `tasks` TEXT NULL DEFAULT NULL,
  `status` VARCHAR(255) NULL DEFAULT 'Pending',
  `appmt_date` DATE NULL DEFAULT NULL,
  `appmt_time` TIME NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 6
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `appointmentspylotdb`.`user`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `appointmentspylotdb`.`user` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL DEFAULT NULL,
  `alias` VARCHAR(255) NULL DEFAULT NULL,
  `email` VARCHAR(255) NULL DEFAULT NULL,
  `password` VARCHAR(255) NULL DEFAULT NULL,
  `dob` DATE NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
