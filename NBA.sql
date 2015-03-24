CREATE SCHEMA NBA;

CREATE TABLE `NBA`.`Commissioner` (
  `commissioner_id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(50) NOT NULL,
  `salary` VARCHAR(45) NOT NULL,
  `start_period` VARCHAR(45) NOT NULL,
  `end_period` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`commissioner_id`));

CREATE TABLE `NBA`.`Schedule` (
  `year` INT NOT NULL,
  PRIMARY KEY (`year`));

CREATE TABLE `NBA`.`Game` (
  `game_id` INT NOT NULL AUTO_INCREMENT,
  `referees` VARCHAR(250) NOT NULL,
  `location` VARCHAR(45) NOT NULL,
  `winner` VARCHAR(45) NOT NULL,
  `score` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`game_id`));

CREATE TABLE `NBA`.`Team` (
  `team_id` INT NOT NULL AUTO_INCREMENT,
  `team_name` VARCHAR(45) NOT NULL,
  `general_manager` VARCHAR(45) NOT NULL,
  `coach` VARCHAR(45) NOT NULL,
  `arena` VARCHAR(45) NOT NULL,
  `record` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`team_id`));

CREATE TABLE `NBA`.`Player` (
  `player_id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `draft_year` INT NOT NULL,
  PRIMARY KEY (`player_id`));

CREATE TABLE `NBA`.`Statistics` (
  `player_id` INT NOT NULL,
  `game_id` INT NOT NULL,
  `field_goal_percentage` INT NOT NULL,
  `turnovers` INT NOT NULL,
  `steals` INT NOT NULL,
  `rebounds` INT NOT NULL,
  `assists` INT NOT NULL,
  `points` INT NOT NULL,
  FOREIGN KEY (player_id) REFERENCES Player(player_id));

CREATE TABLE `NBA`.`Division` (
  `division_id` INT NOT NULL AUTO_INCREMENT,
  `division_name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`division_id`));

  INSERT INTO Commissioner (name, salary, start_period, end_period)
VALUES ('Adam Silver', 4500000, 'May 2014', ‘N/A’);

INSERT INTO Commissioner (name, salary, start_period, end_period)
VALUES ('David Stern', 8500000, 'May 1995', ‘May 2014’);

INSERT INTO Commissioner (name, salary, start_period, end_period)
VALUES ('Ron Smith', 2350000, 'May 1970', ‘May 1995’);

INSERT INTO Division (division_id, division_name)
VALUES (1, 'Atlantic');

INSERT INTO Division (division_id, division_name)
VALUES (2, 'Pacific');

INSERT INTO Division (division_id, division_name)
VALUES (3, 'Southern');

INSERT INTO Game (game_id, location, referees, score, winner)
VALUES (1, ‘Chicago’, 'David Black', ‘100-93’, ‘Chicago’);

INSERT INTO Game (game_id, location, referees, score, winner)
VALUES (2, ‘Toronto’, 'James White', ‘99-68’, ‘Toronto’);

INSERT INTO Game (game_id, location, referees, score, winner)
VALUES (3, ‘Brooklyn’, 'Andrew Gren', ‘74-78’, ‘Miami’);

INSERT INTO Game (game_id, location, referees, score, winner)
VALUES (4, 'Pheonix', 'Charles Tillman', '76-43', 'Pheonix');
INSERT INTO Game (game_id, location, referees, score, winner)
VALUES (5, 'Hamilton', 'Black Smith', '98-54', 'Vancouver');

INSERT INTO Player (draft_year, name, player_id)
VALUES (2005, ‘Kyle Lowry’, 1);

INSERT INTO Player (draft_year, name, player_id)
VALUES (2008, ‘Demar DeRozan’, 2);

INSERT INTO Player (draft_year, name, player_id)
VALUES (2011, ‘Lou Williams’, 3);

INSERT INTO Player (draft_year, name, player_id)
VALUES (2012, 'Brandon C', 4);

INSERT INTO Player (draft_year, name, player_id)
VALUES (2007, 'Tom Jones', 5);

INSERT INTO Player (draft_year, name, player_id)
VALUES (2004, 'LeBron James', 6);

INSERT INTO Player (draft_year, name, player_id)
VALUES (2004, 'Chris Bosh', 8);

INSERT INTO Player (draft_year, name, player_id)
VALUES (2007, 'Landry Fields', 9);

INSERT INTO Player (draft_year, name, player_id)
VALUES (2002, 'Carlos Delfino', 10);


INSERT INTO Schedule (year)
VALUES (2015);

INSERT INTO Schedule (year)
VALUES (2014);

INSERT INTO Schedule (year)
VALUES (2013);

INSERT INTO Statistics (assists, field_goal_percentage, game_id, player_id, points, rebounds, steals, turnovers)
VALUES (5, '50%', 1, 1, 20, 7, 2, 0);
INSERT INTO Statistics (assists, field_goal_percentage, game_id, player_id, points, rebounds, steals, turnovers)
VALUES (8, '23%', 1, 2, 25, 4, 5, 2);

INSERT INTO Statistics (assists, field_goal_percentage, game_id, player_id, points, rebounds, steals, turnovers)
VALUES (2, '24%', 1, 3, 10, 1, 2, 5);

INSERT INTO Statistics (assists, field_goal_percentage, game_id, player_id, points, rebounds, steals, turnovers)
VALUES (6, '55%', 2, 4, 5, 23, 33, 4);

INSERT INTO Statistics (assists, field_goal_percentage, game_id, player_id, points, rebounds, steals, turnovers)
VALUES (1, '56%', 2, 5, 5, 42, 35, 42);

INSERT INTO Statistics (assists, field_goal_percentage, game_id, player_id, points, rebounds, steals, turnovers)
VALUES (8, '40%', 2, 6, 5, 24, 1, 20);

INSERT INTO Statistics (assists, field_goal_percentage, game_id, player_id, points, rebounds, steals, turnovers)
VALUES (10, '73%', 3, 1, 25, 14, 0, 12);

INSERT INTO Statistics (assists, field_goal_percentage, game_id, player_id, points, rebounds, steals, turnovers)
VALUES (15, '33%', 3, 8, 13, 12, 1, 0);

INSERT INTO Statistics (assists, field_goal_percentage, game_id, player_id, points, rebounds, steals, turnovers)
VALUES (20, '23%', 3, 9, 5, 41, 15, 22);

INSERT INTO Statistics (assists, field_goal_percentage, game_id, player_id, points, rebounds, steals, turnovers)
VALUES (5, '82%', 3, 10, 5, 2, 3, 4);

INSERT INTO Team (arena, coach, general_manager, record, team_id, team_name)
VALUES ('Air Canada', 'Dwyane Casey', 'Masai Ujiri', '33-15', 1, 'Raptors');

INSERT INTO Team (arena, coach, general_manager, record, team_id, team_name)
VALUES ('Wells Fargo', 'Tom Thibbadeuo', 'Jones Well', '33-15', 2, 'Bulls');

INSERT INTO Team (arena, coach, general_manager, record, team_id, team_name)
VALUES ('TD Arena', 'Eric Spolstra', 'Wallace Smith', '22-20', 3, 'Miami');