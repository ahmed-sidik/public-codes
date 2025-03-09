const int numberValues[11][8] = {
  {1, 1, 1, 1, 1, 1, 0, 0}, //0
  {0, 1, 1, 0, 0, 0, 0, 0}, //1
  {1, 1, 0, 1, 1, 0, 1, 0}, //2
  {1, 1, 1, 1, 0, 0, 1, 0}, //3
  {0, 1, 1, 0, 0, 1, 1, 0}, //4
  {1, 0, 1, 1, 0, 1, 1, 0}, //5
  {1, 0, 1, 1, 1, 1, 1, 1}, //6
  {1, 1, 1, 0, 0, 0, 0, 0}, //7
  {1, 1, 1, 1, 1, 1, 1, 0}, //8
  {1, 1, 1, 1, 0, 1, 1, 1}, //9
  {0, 0, 0, 0, 0, 0, 0, 0}  //off
};

const int numberPins[8] = {0, 1, 2, 3, 4, 5, 6, 7};
const int numberPinCount = sizeof(numberPins) / sizeof(int);
const int digitPins[4] = {17, 16, 15, 14};
const int digitPinCount = sizeof(digitPins) / sizeof(int);

int digitStates[digitPinCount] = {10, 10, 10, 10};

void updateDisplay() {
  for(int digitIndex = 0; digitIndex < digitPinCount; ++digitIndex) {
    digitalWrite(digitPins[digitIndex], LOW);
  }
  for(int digitIndex = 0; digitIndex < digitPinCount; ++digitIndex) {
    const int number = digitStates[digitIndex];
    for(int i = 0; i < numberPinCount; ++i) {
      digitalWrite(numberPins[i], numberValues[number][i] ? LOW : HIGH);
    }
    digitalWrite(digitPins[digitIndex], HIGH);
    delayMicroseconds(50); // wait for the display to update
    digitalWrite(digitPins[digitIndex], LOW);
  }
  for(int i = 0; i < numberPinCount; ++i) {
    digitalWrite(numberPins[i], HIGH);
  }
}

void setNumber(int number, bool leadingZeros = false) {
  digitStates[3] = number%10;
  digitStates[2] = (number/10)%10;
  digitStates[1] = (number/100)%10;
  digitStates[0] = (number/1000)%10;

  if(leadingZeros) {
    return;
  }

  for(int i=0; i<3; ++i) {
    if(digitStates[i] == 0) {
      digitStates[i] = 10;
    } else {
      break;
    }
  }
}

const int columnPins[4] = {17, 16, 15, 14};
const int columnPinCount = sizeof(columnPins) / sizeof(int);
const int rowPins[4] = {12, 11, 10, 9};
const int rowPinCount = sizeof(rowPins) / sizeof(int);
int previousState[columnPinCount*rowPinCount] = {HIGH};

int getNumber(int keyCode) {
  switch (keyCode)
  {
  case 0:
    return 1;
    break;
  case 4:
    return 2;
    break;
  case 8:
    return 3;
    break;
  case 1:
    return 4;
    break;
  case 5:
    return 5;
    break;
  case 9:
    return 6;
    break;
  case 2:
    return 7;
    break;
  case 6:
    return 8;
    break;
  case 10:
    return 9;
    break;
  case 7:
    return 0;
    break;
  default:
    return -1;
    break;
  }
}

int globalNumber = 0;

void onPress(int keyCode) {
  if((keyCode <= 2 || (4 <= keyCode && keyCode <= 10)) && globalNumber < 1000) {
    globalNumber = globalNumber*10 + getNumber(keyCode);
    setNumber(globalNumber);
  } else if(keyCode == KEYPAD_STAR) {
    globalNumber = 0;
    setNumber(globalNumber);
  }
}

void readInput() {
  for(int column = 0; column < columnPinCount; ++column) {
    digitalWrite(columnPins[column], HIGH);
  }

  for(int column = 0; column < columnPinCount; ++column) {
    digitalWrite(columnPins[column], LOW);
    for(int row = 0; row < rowPinCount; ++row) {
      int reading = digitalRead(rowPins[row]);
      if(reading == LOW && previousState[column*columnPinCount + row] == HIGH) {
        onPress(column*columnPinCount + row);
      }
      previousState[column*columnPinCount + row] = reading;
    }
    digitalWrite(columnPins[column], HIGH);
  }
}

void setup() {
  for(int i = 0; i < numberPinCount; i++) {
    pinMode(numberPins[i], OUTPUT);
  }
  for(int i = 0; i < digitPinCount; i++) {
    pinMode(digitPins[i], OUTPUT);
  }
  for(int i = 0; i < columnPinCount; i++) {
    pinMode(columnPins[i], OUTPUT);
  }
  for(int i = 0; i < rowPinCount; i++) {
    pinMode(rowPins[i], INPUT_PULLUP);
  }

  setNumber(globalNumber);
}

void loop() {
  readInput();
  updateDisplay();
}