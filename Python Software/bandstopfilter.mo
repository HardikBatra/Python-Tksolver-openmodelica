model bandstopfilter
  Modelica.Electrical.Analog.Sensors.VoltageSensor voltageSensor annotation(
    Placement(visible = true, transformation(origin = {116, 36}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Electrical.Analog.Sources.SineVoltage sineVoltage(V = 1, freqHz = 1)  annotation(
    Placement(visible = true, transformation(origin = {-116, -12}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Electrical.Analog.Ideal.IdealOpAmp3Pin opAmp annotation(
    Placement(visible = true, transformation(origin = {-16, 52}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Electrical.Analog.Ideal.IdealOpAmp3Pin opAmp1 annotation(
    Placement(visible = true, transformation(origin = {-18, -50}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Electrical.Analog.Ideal.IdealOpAmp3Pin opAmp2 annotation(
    Placement(visible = true, transformation(origin = {76, 36}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Electrical.Analog.Basic.Capacitor CH annotation(
    Placement(visible = true, transformation(origin = {-84, -38}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Electrical.Analog.Basic.Capacitor CL annotation(
    Placement(visible = true, transformation(origin = {-56, 10}, extent = {{-10, -10}, {10, 10}}, rotation = -90)));
  Modelica.Electrical.Analog.Basic.Resistor RH annotation(
    Placement(visible = true, transformation(origin = {-54, -66}, extent = {{-10, -10}, {10, 10}}, rotation = -90)));
  Modelica.Electrical.Analog.Basic.Resistor RL annotation(
    Placement(visible = true, transformation(origin = {-84, 40}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Electrical.Analog.Basic.Resistor R1 annotation(
    Placement(visible = true, transformation(origin = {26, -50}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Electrical.Analog.Basic.Resistor R2 annotation(
    Placement(visible = true, transformation(origin = {30, 52}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Electrical.Analog.Basic.Resistor R3 annotation(
    Placement(visible = true, transformation(origin = {76, 74}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Electrical.Analog.Basic.Ground ground annotation(
    Placement(visible = true, transformation(origin = {-134, -68}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Electrical.Analog.Interfaces.Pin pin annotation(
    Placement(visible = true, transformation(origin = {98, 36}, extent = {{-6, -6}, {6, 6}}, rotation = 0), iconTransformation(origin = {98, 36}, extent = {{-6, -6}, {6, 6}}, rotation = 0)));
  Modelica.Electrical.Analog.Interfaces.Pin pin1 annotation(
    Placement(visible = true, transformation(origin = {51, 53}, extent = {{-5, -5}, {5, 5}}, rotation = 0), iconTransformation(origin = {51, 53}, extent = {{-5, -5}, {5, 5}}, rotation = 0)));
  Modelica.Electrical.Analog.Interfaces.Pin pin2 annotation(
    Placement(visible = true, transformation(origin = {6, 52}, extent = {{-6, -6}, {6, 6}}, rotation = 0), iconTransformation(origin = {6, 52}, extent = {{-6, -6}, {6, 6}}, rotation = 0)));
  Modelica.Electrical.Analog.Interfaces.Pin pin3 annotation(
    Placement(visible = true, transformation(origin = {4, -50}, extent = {{-6, -6}, {6, 6}}, rotation = 0), iconTransformation(origin = {4, -50}, extent = {{-6, -6}, {6, 6}}, rotation = 0)));
  Modelica.Electrical.Analog.Interfaces.Pin pin4 annotation(
    Placement(visible = true, transformation(origin = {-55, 39}, extent = {{-5, -5}, {5, 5}}, rotation = 0), iconTransformation(origin = {-55, 39}, extent = {{-5, -5}, {5, 5}}, rotation = 0)));
  Modelica.Electrical.Analog.Interfaces.Pin pin5 annotation(
    Placement(visible = true, transformation(origin = {-55, -49}, extent = {{-5, -5}, {5, 5}}, rotation = 0), iconTransformation(origin = {-55, -49}, extent = {{-5, -5}, {5, 5}}, rotation = 0)));
  Modelica.Electrical.Analog.Interfaces.Pin pin6 annotation(
    Placement(visible = true, transformation(origin = {-95, -13}, extent = {{-5, -5}, {5, 5}}, rotation = 0), iconTransformation(origin = {-95, -13}, extent = {{-5, -5}, {5, 5}}, rotation = 0)));
  Modelica.Electrical.Analog.Basic.Ground ground1 annotation(
    Placement(visible = true, transformation(origin = {-56, -20}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Electrical.Analog.Basic.Ground ground2 annotation(
    Placement(visible = true, transformation(origin = {-54, -94}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Electrical.Analog.Basic.Ground ground3 annotation(
    Placement(visible = true, transformation(origin = {50, 10}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Electrical.Analog.Basic.Ground ground4 annotation(
    Placement(visible = true, transformation(origin = {126, -20}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
equation
  connect(sineVoltage.p, ground.p) annotation(
    Line(points = {{-126, -12}, {-134, -12}, {-134, -58}}, color = {0, 0, 255}));
  connect(sineVoltage.n, pin6) annotation(
    Line(points = {{-106, -12}, {-106, -11}, {-94, -11}, {-94, -12}}, color = {0, 0, 255}));
  connect(RL.p, pin6) annotation(
    Line(points = {{-94, 40}, {-94, -12}}, color = {0, 0, 255}));
  connect(pin6, CH.p) annotation(
    Line(points = {{-94, -12}, {-94, -38}}, color = {0, 0, 255}));
  connect(CH.n, pin5) annotation(
    Line(points = {{-74, -38}, {-66, -38}, {-66, -48}, {-54, -48}}, color = {0, 0, 255}));
  connect(pin5, RH.p) annotation(
    Line(points = {{-54, -48}, {-54, -56}}, color = {0, 0, 255}));
  connect(pin5, opAmp1.in_p) annotation(
    Line(points = {{-54, -48}, {-40, -48}, {-40, -56}, {-28, -56}, {-28, -56}}, color = {0, 0, 255}));
  connect(opAmp1.in_n, pin3) annotation(
    Line(points = {{-28, -44}, {-34, -44}, {-34, -24}, {4, -24}, {4, -50}}, color = {0, 0, 255}));
  connect(opAmp1.out, pin3) annotation(
    Line(points = {{-8, -50}, {4, -50}}, color = {0, 0, 255}));
  connect(pin3, R1.p) annotation(
    Line(points = {{4, -50}, {16, -50}}, color = {0, 0, 255}));
  connect(opAmp.in_n, pin2) annotation(
    Line(points = {{-26, 58}, {-46, 58}, {-46, 72}, {6, 72}, {6, 52}}, color = {0, 0, 255}));
  connect(opAmp.out, pin2) annotation(
    Line(points = {{-6, 52}, {6, 52}}, color = {0, 0, 255}));
  connect(pin2, R2.p) annotation(
    Line(points = {{6, 52}, {20, 52}}, color = {0, 0, 255}));
  connect(opAmp.in_p, pin4) annotation(
    Line(points = {{-26, 46}, {-54, 46}, {-54, 40}}, color = {0, 0, 255}));
  connect(pin4, CL.p) annotation(
    Line(points = {{-54, 40}, {-56, 40}, {-56, 20}}, color = {0, 0, 255}));
  connect(RL.n, pin4) annotation(
    Line(points = {{-74, 40}, {-54, 40}}, color = {0, 0, 255}));
  connect(CL.n, ground1.p) annotation(
    Line(points = {{-56, 0}, {-56, -10}}, color = {0, 0, 255}));
  connect(RH.n, ground2.p) annotation(
    Line(points = {{-54, -76}, {-54, -84}}, color = {0, 0, 255}));
  connect(opAmp2.in_p, ground3.p) annotation(
    Line(points = {{66, 30}, {50, 30}, {50, 20}}, color = {0, 0, 255}));
  connect(R2.n, pin1) annotation(
    Line(points = {{40, 52}, {48, 52}, {48, 53}, {51, 53}}, color = {0, 0, 255}));
  connect(pin1, opAmp2.in_n) annotation(
    Line(points = {{51, 53}, {66, 53}, {66, 42}}, color = {0, 0, 255}));
  connect(R3.p, pin1) annotation(
    Line(points = {{66, 74}, {51, 74}, {51, 53}}, color = {0, 0, 255}));
  connect(R3.n, pin) annotation(
    Line(points = {{86, 74}, {98, 74}, {98, 36}}, color = {0, 0, 255}));
  connect(opAmp2.out, pin) annotation(
    Line(points = {{86, 36}, {98, 36}}, color = {0, 0, 255}));
  connect(pin, voltageSensor.p) annotation(
    Line(points = {{98, 36}, {106, 36}}, color = {0, 0, 255}));
  connect(voltageSensor.n, ground4.p) annotation(
    Line(points = {{126, 36}, {126, -10}}, color = {0, 0, 255}));
  connect(R1.n, pin1) annotation(
    Line(points = {{36, -50}, {34, -50}, {34, 40}, {52, 40}, {52, 54}}, color = {0, 0, 255}));

annotation(
    uses(Modelica(version = "3.2.3")),
    Diagram(graphics = {Text(origin = {-35, 91}, extent = {{-17, 3}, {89, -7}}, textString = "BAND STOP FILTER", textStyle = {TextStyle.Italic, TextStyle.Italic, TextStyle.Italic, TextStyle.Italic, TextStyle.Italic, TextStyle.Italic, TextStyle.Italic, TextStyle.Italic})}));
end bandstopfilter;
