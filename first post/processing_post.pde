class MyParticle {
  PVector pos = new PVector(random(55, 445), random(55, 445));
  PVector vel = PVector.random2D();
  PVector center = new PVector(250, 250);
  float pColour = random(0,255);
  float eS;
  float distance = random(0,255);  

  void update(PVector mouseVector){
    PVector tmp = PVector.add(mouseVector, vel);
    tmp.setMag(tmp.mag()*1);
    pos.add(tmp);
    float d = PVector.dist(pos, center);
    eS = (200-d)*0.05;
    if (eS < 1) {
      pos = new PVector(random(55, 445), random(55, 445));
      vel = PVector.random2D();
    }
  }

  void render() {
    fill(pColour, 100);
    ellipse(pos.x, pos.y, eS, eS);
  }

  boolean isDraw(MyParticle input){
    return (PVector.dist(pos, input.pos) < 50);
  }
}


MyParticle[] objArray = new MyParticle[150];  

void setup() {
  size(500, 500);
  for (int i = 0; i < objArray.length; i = i + 1) {
    objArray[i] = new MyParticle();
  }
  noStroke();
}

void update() {
  PVector v1 = new PVector(pmouseX, pmouseY);
  PVector v2 = new PVector(mouseX, mouseY);
  PVector v3 = PVector.sub(v2,v1);
  
  for (int i = 0; i < objArray.length; i = i + 1) {
    objArray[i].update(v3);
  }
}

void render() {
  background(0);
  stroke(255,100);
  strokeWeight(1);
  for (int i = 0; i < objArray.length; i = i + 1){
    for (int j = 0; j < objArray.length; j = j + 1){
      if (  objArray[i].isDraw(objArray[j])) {
        line(objArray[i].pos.x, objArray[i].pos.y, objArray[j].pos.x, objArray[j].pos.y);
      }
    }
  }

  for (MyParticle tmp : objArray) {
    tmp.render();
  }
}

void draw() {
  update();
  render();
}
