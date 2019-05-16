// PLANETARY DEFENSE 

// OBJECTIVE: Protect the planet! Use mankind's strongest laser to destroy incoming asteroids and save the world from total annihilation.
// PRESS F TO START THE GAME
// CONTROLS: 
//   - WASD moves the planet
//   - Left Mouse Button fires laser 



int planetX = 200; // Sets initial X Coordinate for the planet
int planetY = 200; // Sets initial Y Coordinate for the planet
int size = 50;
int astSize = 20;
int targetX = 0;
int targetY = 0;  
boolean astStart = false;
boolean ast1Spawn = false;
boolean startState = true;
boolean level2 = false;
float astXGlob;
float astYGlob;
int moveUp = 0; 
int moveDown = 0; 
int moveRight = 0;
int moveLeft = 0;
int killCount = 0;
float a = random(400); //randomizes x position of moving stars
float b = random(400);
float c = random(400);
float d = random(400);
float e = random(400);
int m = 0; //initializes coordinates for moving stars
float n = 0;
float p = 0;
float q = 0;
int o = 0;
int s = 0;

class Asteroid {
  float astX;
  float astY;
  boolean Spawn = true;

  Asteroid() {
    astX = random(0, 400); //randomizes where asteroids originate
    astY = random(0, 400);
  }
  
  void draw() {
    fill(118, 94, 78); //brownish atseroids
    if (Spawn == true) {
      rect(astX, astY, astSize, astSize);
    }

    if (targetX >= astX-astSize && targetX <= astX+astSize) { // if the laser hits the asteroid, despawn asteroid
      if (targetY >=astY-astSize && targetY <= astY+astSize) {
        Spawn = false;
      }
    }
  }

  void move() {
    if (Spawn == true) {
      if (astX < planetX) {
        astX += .5;
      } 
      if (astX > planetX) {
        astX -= .5;
      } 
      if (astY < planetY) {
        astY += .5;
      }
      if (astY > planetY) {
        astY -= .5;
      }
      if (astX < (planetX+20) && astX > (planetX-20)) { //if the asteroid hits the planet = GAME OVER!
        if (astY < (planetY+20) && astY > (planetY-20)) {
          fill(0, 255, 0);
          textSize(50);
          textAlign(CENTER);
          text("GAME OVER", 200, 200);
        }
      }
    }
  }
}

Asteroid ast1, ast2, ast3, ast4, ast5;


void setup() {
  size(400, 400);  // Makes canvas size 400 by 400 units
  ellipseMode(CENTER); // Sets ellipse draw mode to "CENTER"
  rectMode(CENTER); // Sets rectangle draw mode to "CENTER"
  ast1 = new Asteroid();
  ast2 = new Asteroid();
  ast3 = new Asteroid();
  ast4 = new Asteroid();
  ast5 = new Asteroid();
}

void draw() {
  background(0); // Black background 
  
  //moving stars
  stroke(255);
  line(s, a, m, a);
  line(s, b, n, b);
  line(s, c, o, c);
  line(s, d, p, d);
  line(s, e, q, e);
  m = m + 1;
  n = n + 0.5;
  o = o + 1;
  p = p + 0.75;
  q = q + 0.5;
  noStroke();
 
  //planet
  fill(73, 118, 117); // gray Fill for planet
  ellipse(planetX, planetY, size, size);  // Draws the planet every frame at (planetX, planetY) with a width and height of  "Size"
  stroke(255,0,0);
  line(planetX-25, planetY-25, planetX+25, planetY+25);
  noStroke();


  
  if (moveUp == 1) { 
    planetY = planetY - 1; //pressing "w" makes moveUp true, moving planet up
  } 

  if (moveDown == 1) {
    planetY = planetY + 1; //pressing "s" makes moveDown true, moving planet down
  } 

  if (moveRight == 1) {
    planetX = planetX + 1; //pressing "d" makes moveRight true, moving planet right
  } 


  if (moveLeft == 1) {
    planetX = planetX - 1; //pressing "a" makes moveLeft true, moving planet left
  } 
  

  if (astStart == true) {
    if (ast1Spawn == true) {
      ast1.draw();
      ast1.move();
      ast2.draw();
      ast3.draw();
      ast4.draw();
      ast5.draw();
      ast2.move();
      ast3.move();
      ast4.move();
      ast5.move();
    }

    //target that follows mouse for shooting laser
    fill(0, 255, 0);
    rect(mouseX-20, mouseY, 10, 10);
    rect(mouseX+20, mouseY, 10, 10);
    rect(mouseX, mouseY-20, 10, 10);
    rect(mouseX, mouseY+20, 10, 10);


    //draws laser from planet to where mouse clicks
    if (mousePressed == true) { 
      stroke(0, 255, 0);
      line(planetX, planetY, targetX, targetY);
      stroke(0);
    }
  }
}

void keyPressed() { 
  
  //using w, a, s, and d will act as arrows and move planet around
  //w moves planet up
  if (key == 'w') {
    if (moveUp == 0) {
      moveUp = 1;
    } else if (moveUp == 1) {
      moveUp = 0;
    }
  }

  //a moves planet left
  if (key == 'a') {
    if (moveLeft == 0) {
      moveLeft = 1;
    } else if (moveLeft == 1) {
      moveLeft = 0;
    }
  }

  //s moves planet down
  if (key == 's') {
    if (moveDown == 0) {
      moveDown = 1;
    } else if (moveDown == 1) {
      moveDown = 0;
    }
  }

  //d moves planet down
  if (key == 'd') {
    if (moveRight == 0) {
      moveRight = 1;
    } else if (moveRight == 1) {
      moveRight = 0;
    }
  }

  // "f" KEY starts game (launches atseroids)
  if (key == 'f') {
    astStart = true;
    ast1Spawn = true;
    startState = false;
  }
}

//shoots laser
void mousePressed() {
  targetX = mouseX;
  targetY = mouseY;
}