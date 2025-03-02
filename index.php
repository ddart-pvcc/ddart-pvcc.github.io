<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width">
        <title> My First Amazing PHP Page! </title>
    
        <body>

            <h1>Welcome to My First PHP Page!</h1>
            <p>This is a simple webpage with PHP.</p>
    
            <p>Zombie Apocoalypse says, "<?php echo 'Hello World!'; ?>"</p>
            
            <h3>

            
            <h1>Smash Zombies</h1>
            <?php
            

            ?>
                
            <h1>Loops</h1>
           <?php
                /**
                 *  1. Play with the length of the loop.
                 * Try out different increments like i =+ 2 or i -=37.
                 */
                $horde = 0;
                $humans = 100;
                echo "<br> Before Increment Loop: <br>";
                echo "Horde: " . $horde . " Humans: " . $humans;
                for( $i = 0; $i < 6; $i++){
                    $horde += 2;
                    $humans -=10;
                }
                echo "<br> After Loop <br>";
                echo "Horde " . $horde . " Humans: " . $humans;
            
                //decrement loop

                $horde = 0;
                $humans = 100;
                echo "<br><br>Before Decrement Loop: <br>";
                echo "Horde: " . $horde . " Humans: " . $humans;
                for ( $j = 6; $j >= 1; $j--) {
                    $horde += 10;
                    $humans -=30;
                }
                echo "<br> After Loop <br>";
                echo "Horde " . $horde . " Humans: " . $humans;
            
            /*
                $george = "zombie";
                $stillAZombie = true;
                while( $stillAZombie ) {
                    if( $george == "zombie" ) {
                        echo "Trying Cure... <br>";
                        $george = tryToCure( $george );
                    } else {
                        echo "Cured! <br>";
                        $stillAZombie = false; 
                    }
                }
            
            function tryToCure( $person ) {
                $result = rand(0, 100);
                if($result <= 10) {
                    return "HUMAN";
                }
                else {
                    return "zombie";
                }

            }
            
            */
            /**
                  Experiments to try:
                    1. Add four 1's and two 0's into the horde array. How does that change the output?
                    2. What happens if you set the conditional higher thn the horde array's length?
                    3. What happens if you start i at 1? or 2? or 7?
            */
            ?>
            <h1>Arrays</h1>
            <?php
            $horde = [1, 0, 0, 1, 1];
            $results = [];
            for($i = 0; $i < count($horde); $i++){
                $results[$i] = tryToCure( $horde[$i]);
            }
            echo "<br>Results array:<br>";
            print_r($results);

            function tryToCure($person){
                $result = rand(0,100) * $person;
                if($result <= 10){
                    return " cured!";
                } else {
                    return " still a zombie";
                }
            }

            /**
                  Experiments to try:
                    1. Remove the comment on the second patientList. Does the program break?
                    2. Rewrite the program so that it can sort 0's as zombies, 1's as humans and 2's as infected. Then uncomment patientList Number 3
            */
            ?>
            <h1>Sorting</h1>
            <?php
            $patientList = [1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0];
            $i = 0;

            $humans = 0;
            $zombies = 0;
            while ($i < count($patientList)){
                if( $patientList[$i] ==1) {
                    $humans++;
                } else {
                    $zombies++;
                }
                $i++;
            }

            echo "<br>Humans: " . $humans . " Zombies: " . $zombies;


            ?>
            <h1>Scope</h1>
            <?php
            $zombie = "Fred";
            function zombieName() {
                global $zombie;
                $undead = "Jamal";
                echo "<h2>Inside Function:</h2>";
                echo "Zombie's name: " . $zombie . "<br>";
                echo "Undead's name:" . $undead . "<br>";
            }
            zombieName();
            echo "<h2>Outside function:</h2>";
            echo "Zombie's name: " . $zombie . "<br>";
            echo "Undead's name: " . $undead . "<br>";


            ?>
            
            </h3>

            
            
            
            
            
            <h1>Math</h1>
            <?php 
                // math in php
                $zombies = 1000000;
                $infected = 1000;
                $cured = 75;
                $humans = 1000000;
                $infectionRate = 0.80;
                $antidote = 10;
                $hordeSize = 10007;
                $undead = $zombies + $infected;
                echo "Addition " . $undead . "<br>";
                $undead = $zombies - $cured;
                echo "Subtraction: " . $undead . "<br>";
                $undead = $humans * $infectionRate;
                echo "Multiplication: " . $undead . "<br>";
                $undead = $zombies / $antidote;
                echo "Division: " . $undead . "<br>";
                $nextHorde = $zombies % $hordeSize;
                echo "Modulus: " . $nextHorde . "<br>";
            
                // += variations

                $golfScore = 3;
                echo "Score: " . $golfScore . "<br>";
                $golfScore = $golfScore + 6;
                echo "Score: " . $golfScore . "<br>";
                $golfScore += 4;
                echo "Score: " . $golfScore . "<br>";
                $golfScore = $golfScore -1;
                echo "Score: " . $golfScore . "<br>";
                $golfScore -= 1; 
                echo "Score: " . $golfScore . "<br>";
                $golfScore++;
                echo "Score: " . $golfScore . "<br>";
                $golfScore --;
            ?>
            
            <p>Golf Score: <?php echo $golfScore;?></p>

            <?php

                $golfScore = 37;
                echo $golfScore;
                $par = 36 + $golfScore++;
                echo "<br>";
                echo $par;
                echo "<br>";

                $golfScore = 37;
                echo $golfScore;
                echo "<br>";
                $par = 36 + ++$golfScore;
                echo $par;

            ?>

            <h1>Logic:</h1>
            <h2>Conditional Test:
                <?php
                    $score = 25;
                    if($score == 25) {
                        echo $score."<br>";
                    }
                    if($score==='25'){
                        echo $score; 
                    } else {
                        echo "The number 25 is not === to the string 25".'<br>';
                    }
                    
                    $score = 0;
                    if ($score){
                        echo $score . " is True.";
                    }
                    else {
                        echo $score . " is False.";
                    }

                ?>
            
            Loops:<br>

            For Loop:
            <br>
            Zombies!
            </h2>
                

            <?php
                $zombie = 1;
                for( $i = 0; $i < 10; $i++ ){
                    $zombie *= ($i + 1);
                    echo $zombie;
                    echo "<br>";
                }
                
                for($i = 0; $i < 5; $i++){
                    echo "hello from a php for loop" . '<br>';
                }
            ?>
            
            <br><h2>While Loop</h2> 
            
             <?php
                $j = 5;
                while($j > 1){
                    echo "hello from a php while loop" . '<br>';
                    $j--;
                }
            ?>
            <br><h2>Do Loop</h2> 
            
            <?php
               $k = 5;
               do{ echo "hello from a php do loop" . '<br>';
                   $k--;
               } while($k> 5)
           ?>
           <br><h2>Arrays</h2> 
            
            <?php
               $guitars = [];
               $guitars[0] = "Stratocaster";
               $guitars[1] = "Gibson";
               echo $guitars[0] ."<br>";
               echo $guitars[1].'<br>';
               
               $horde = ['Bob', 'Fred', 'Leroy'];
               $zombie = $horde[2][2];
               echo $zombie;
               
               foreach ($horde as $name) {

                for ($i = 0; $i < strlen($name); $i++){
                    echo $name[$i]."\n";
                }
               }
                    
           ?>
                    </body>
    </head>
</html>


