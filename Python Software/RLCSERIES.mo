model RLCSERIES
  Modelica.Electrical.Analog.Basic.Resistor resistor annotation(
    Placement(visible = true, transformation(origin = {-54, 40}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Electrical.Analog.Basic.Capacitor capacitor annotation(
    Placement(visible = true, transformation(origin = {54, 40}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Electrical.Analog.Basic.Inductor inductor annotation(
    Placement(visible = true, transformation(origin = {0, 40}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Electrical.Analog.Sources.SineVoltage sineVoltage(V = 100, freqHz = 50)  annotation(
    Placement(visible = true, transformation(origin = {-80, 4}, extent = {{-10, -10}, {10, 10}}, rotation = -90)));
  Modelica.Electrical.Analog.Basic.Ground ground annotation(
    Placement(visible = true, transformation(origin = {0, -62}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Electrical.Analog.Sensors.CurrentSensor currentSensor annotation(
    Placement(visible = true, transformation(origin = {80, 2}, extent = {{-10, -10}, {10, 10}}, rotation = -90)));
equation
  connect(resistor.n, inductor.p) annotation(
    Line(points = {{-44, 40}, {-10, 40}}, color = {0, 0, 255}));
  connect(inductor.n, capacitor.p) annotation(
    Line(points = {{10, 40}, {44, 40}}, color = {0, 0, 255}));
  connect(resistor.p, sineVoltage.p) annotation(
    Line(points = {{-64, 40}, {-81, 40}, {-81, 14}, {-80, 14}}, color = {0, 0, 255}));
  connect(capacitor.n, currentSensor.p) annotation(
    Line(points = {{64, 40}, {80, 40}, {80, 12}, {80, 12}, {80, 12}}, color = {0, 0, 255}));
  connect(currentSensor.n, ground.p) annotation(
    Line(points = {{80, -8}, {80, -52}, {0, -52}}, color = {0, 0, 255}));
  connect(sineVoltage.n, ground.p) annotation(
    Line(points = {{-80, -6}, {-80, -52}, {0, -52}}, color = {0, 0, 255}));
  annotation(
    uses(Modelica(version = "3.2.3")),
    Diagram(graphics = {Text(origin = {-18, 82}, extent = {{-44, 10}, {78, -6}}, textString = "RLC SERIES", textStyle = {TextStyle.Italic, TextStyle.Italic, TextStyle.Italic, TextStyle.Italic, TextStyle.Italic, TextStyle.Italic, TextStyle.Italic, TextStyle.Italic})}));
end RLCSERIES;
