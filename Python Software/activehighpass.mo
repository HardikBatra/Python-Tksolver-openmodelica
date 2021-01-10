model activehighpass
  Modelica.Electrical.Analog.Basic.Capacitor c1 annotation(
    Placement(visible = true, transformation(origin = {-42, 28}, extent = {{10, -10}, {-10, 10}}, rotation = 0)));
  Modelica.Electrical.Analog.Ideal.IdealOpAmp3Pin opAmp annotation(
    Placement(visible = true, transformation(origin = {34, 22}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Electrical.Analog.Basic.Resistor r1 annotation(
    Placement(visible = true, transformation(origin = {-16, -8}, extent = {{-10, -10}, {10, 10}}, rotation = -90)));
  Modelica.Electrical.Analog.Basic.Resistor r2 annotation(
    Placement(visible = true, transformation(origin = {22, -44}, extent = {{10, -10}, {-10, 10}}, rotation = -90)));
  Modelica.Electrical.Analog.Basic.Resistor r3 annotation(
    Placement(visible = true, transformation(origin = {56, -4}, extent = {{10, -10}, {-10, 10}}, rotation = 0)));
  Modelica.Electrical.Analog.Sources.SineVoltage sineVoltage(V = 1, freqHz = 10000)  annotation(
    Placement(visible = true, transformation(origin = {-80, 28}, extent = {{10, -10}, {-10, 10}}, rotation = 0)));
  Modelica.Electrical.Analog.Interfaces.Pin pin annotation(
    Placement(visible = true, transformation(origin = {-15, 29}, extent = {{-5, -5}, {5, 5}}, rotation = 0), iconTransformation(origin = {-30, 32}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Electrical.Analog.Interfaces.Pin pin1 annotation(
    Placement(visible = true, transformation(origin = {21, -5}, extent = {{-7, -7}, {7, 7}}, rotation = 0), iconTransformation(origin = {-10, 32}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Electrical.Analog.Basic.Ground ground annotation(
    Placement(visible = true, transformation(origin = {-90, -30}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Electrical.Analog.Basic.Ground ground1 annotation(
    Placement(visible = true, transformation(origin = {-16, -80}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
equation
  connect(sineVoltage.n, ground.p) annotation(
    Line(points = {{-90, 28}, {-90, -20}}, color = {0, 0, 255}));
  connect(pin, opAmp.in_n) annotation(
    Line(points = {{-14, 30}, {24, 30}, {24, 28}, {24, 28}}, color = {0, 0, 255}));
  connect(sineVoltage.p, c1.n) annotation(
    Line(points = {{-70, 28}, {-52, 28}, {-52, 28}, {-52, 28}}, color = {0, 0, 255}));
  connect(c1.p, pin) annotation(
    Line(points = {{-32, 28}, {-14, 28}, {-14, 30}, {-14, 30}}, color = {0, 0, 255}));
  connect(r1.n, ground1.p) annotation(
    Line(points = {{-16, -18}, {-16, -18}, {-16, -70}, {-16, -70}}, color = {0, 0, 255}));
  connect(r1.p, pin) annotation(
    Line(points = {{-16, 2}, {-16, 2}, {-16, 30}, {-14, 30}}, color = {0, 0, 255}));
  connect(pin1, r2.n) annotation(
    Line(points = {{22, -4}, {22, -4}, {22, -34}, {22, -34}}, color = {0, 0, 255}));
  connect(r2.p, ground1.p) annotation(
    Line(points = {{22, -54}, {22, -54}, {22, -70}, {-16, -70}, {-16, -70}}, color = {0, 0, 255}));
  connect(pin1, opAmp.in_p) annotation(
    Line(points = {{22, -4}, {20, -4}, {20, 16}, {24, 16}, {24, 16}}, color = {0, 0, 255}));
  connect(r3.n, pin1) annotation(
    Line(points = {{46, -4}, {20, -4}, {20, -4}, {22, -4}}, color = {0, 0, 255}));
  connect(opAmp.out, r3.p) annotation(
    Line(points = {{44, 22}, {74, 22}, {74, -4}, {66, -4}, {66, -4}}, color = {0, 0, 255}));
  annotation(
    uses(Modelica(version = "3.2.3")),
    Diagram(graphics = {Text(origin = {1, 74}, extent = {{-69, 16}, {69, -16}}, textString = "ACTIVE HIGH PASS FILTER FIRST ORDER", textStyle = {TextStyle.Italic, TextStyle.Italic})}, coordinateSystem(initialScale = 0.1)));
end activehighpass;
