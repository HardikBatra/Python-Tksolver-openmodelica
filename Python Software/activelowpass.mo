model activelowpass
  Modelica.Electrical.Analog.Basic.Ground ground annotation(
    Placement(visible = true, transformation(origin = {-86, 20}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Electrical.Analog.Basic.Resistor R3(R = 4000)  annotation(
    Placement(visible = true, transformation(origin = {22, 56}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Electrical.Analog.Basic.Resistor R2(R = 1000)  annotation(
    Placement(visible = true, transformation(origin = {-58, 42}, extent = {{10, -10}, {-10, 10}}, rotation = 0)));
  Modelica.Electrical.Analog.Basic.Ground ground1 annotation(
    Placement(visible = true, transformation(origin = {-28, -88}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Electrical.Analog.Ideal.IdealOpAmp3Pin opAmp annotation(
    Placement(visible = true, transformation(origin = {20, 6}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Electrical.Analog.Basic.Capacitor C1(C = 6.8e-8)  annotation(
    Placement(visible = true, transformation(origin = {-28, -34}, extent = {{-10, -10}, {10, 10}}, rotation = 90)));
  Modelica.Electrical.Analog.Interfaces.Pin pin1 annotation(
    Placement(visible = true, transformation(origin = {-26, 42}, extent = {{-4, -4}, {4, 4}}, rotation = 0), iconTransformation(origin = {-26, 42}, extent = {{-4, -4}, {4, 4}}, rotation = 0)));
  Modelica.Electrical.Analog.Interfaces.Pin pin2 annotation(
    Placement(visible = true, transformation(origin = {-30, 2}, extent = {{-4, -4}, {4, 4}}, rotation = 0), iconTransformation(origin = {-30, 2}, extent = {{-4, -4}, {4, 4}}, rotation = 0)));
  Modelica.Electrical.Analog.Sources.SineVoltage sineVoltage(V = 1, freqHz = 160)  annotation(
    Placement(visible = true, transformation(origin = {-90, -40}, extent = {{10, -10}, {-10, 10}}, rotation = 90)));
  Modelica.Electrical.Analog.Interfaces.Pin pin annotation(
    Placement(visible = true, transformation(origin = {54, 6}, extent = {{-4, -4}, {4, 4}}, rotation = 0), iconTransformation(origin = {54, 6}, extent = {{-4, -4}, {4, 4}}, rotation = 0)));
  Modelica.Electrical.Analog.Sensors.VoltageSensor voltageSensor annotation(
    Placement(visible = true, transformation(origin = {80, -46}, extent = {{-14, -14}, {14, 14}}, rotation = -90)));
  Modelica.Electrical.Analog.Basic.Resistor R1(R = 15000)  annotation(
    Placement(visible = true, transformation(origin = {-68, 0}, extent = {{10, -10}, {-10, 10}}, rotation = 0)));
equation
  connect(R2.p, ground.p) annotation(
    Line(points = {{-48, 42}, {-86, 42}, {-86, 30}}, color = {0, 0, 255}));
  connect(R2.n, pin1) annotation(
    Line(points = {{-68, 42}, {-26, 42}}, color = {0, 0, 255}));
  connect(R3.p, pin1) annotation(
    Line(points = {{12, 56}, {-26, 56}, {-26, 42}}, color = {0, 0, 255}));
  connect(pin1, opAmp.in_n) annotation(
    Line(points = {{-26, 42}, {-26, 12}, {10, 12}}, color = {0, 0, 255}));
  connect(opAmp.in_p, pin2) annotation(
    Line(points = {{10, 0}, {-9, 0}, {-9, 2}, {-30, 2}}, color = {0, 0, 255}));
  connect(R3.n, pin) annotation(
    Line(points = {{32, 56}, {54, 56}, {54, 6}}, color = {0, 0, 255}));
  connect(opAmp.out, pin) annotation(
    Line(points = {{30, 6}, {54, 6}}, color = {0, 0, 255}));
  connect(voltageSensor.p, pin) annotation(
    Line(points = {{80, -32}, {80, 6}, {54, 6}}, color = {0, 0, 255}));
  connect(voltageSensor.n, ground1.p) annotation(
    Line(points = {{80, -60}, {80, -78}, {-28, -78}}, color = {0, 0, 255}));
  connect(sineVoltage.n, ground1.p) annotation(
    Line(points = {{-90, -50}, {-90, -78}, {-28, -78}}, color = {0, 0, 255}));
  connect(C1.n, pin2) annotation(
    Line(points = {{-28, -24}, {-28, -12}, {-30, -12}, {-30, 2}}, color = {0, 0, 255}));
  connect(C1.p, ground1.p) annotation(
    Line(points = {{-28, -44}, {-28, -78}}, color = {0, 0, 255}));
  connect(R1.p, pin2) annotation(
    Line(points = {{-58, 0}, {-43, 0}, {-43, 2}, {-30, 2}}, color = {0, 0, 255}));
  connect(R1.n, sineVoltage.p) annotation(
    Line(points = {{-78, 0}, {-90, 0}, {-90, -30}, {-90, -30}}, color = {0, 0, 255}));
  annotation(
    uses(Modelica(version = "3.2.3")),
    Diagram(graphics = {Text(origin = {-27, 93}, extent = {{-17, 5}, {77, -7}}, textString = "ACTIVE LOW PASS FILTER", textStyle = {TextStyle.Italic, TextStyle.Italic})}));
end activelowpass;
