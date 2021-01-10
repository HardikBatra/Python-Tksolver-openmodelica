model activelowpassSecondOrder
  Modelica.Electrical.Analog.Basic.Resistor R1 annotation(
    Placement(visible = true, transformation(origin = {12, -50}, extent = {{10, -10}, {-10, 10}}, rotation = -90)));
  Modelica.Electrical.Analog.Basic.Resistor R2 annotation(
    Placement(visible = true, transformation(origin = {40, -24}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Electrical.Analog.Basic.Resistor R3 annotation(
    Placement(visible = true, transformation(origin = {-80, 16}, extent = {{10, -10}, {-10, 10}}, rotation = 0)));
  Modelica.Electrical.Analog.Basic.Resistor R4 annotation(
    Placement(visible = true, transformation(origin = {-42, 16}, extent = {{10, -10}, {-10, 10}}, rotation = 0)));
  Modelica.Electrical.Analog.Basic.Capacitor C1 annotation(
    Placement(visible = true, transformation(origin = {32, 50}, extent = {{10, -10}, {-10, 10}}, rotation = 0)));
  Modelica.Electrical.Analog.Basic.Capacitor C2 annotation(
    Placement(visible = true, transformation(origin = {-18, -32}, extent = {{10, -10}, {-10, 10}}, rotation = 90)));
  Modelica.Electrical.Analog.Sensors.VoltageSensor voltageSensor annotation(
    Placement(visible = true, transformation(origin = {82, -36}, extent = {{-10, -10}, {10, 10}}, rotation = -90)));
  Modelica.Electrical.Analog.Sources.SineVoltage sineVoltage(V = 1, freqHz = 1)  annotation(
    Placement(visible = true, transformation(origin = {-94, -30}, extent = {{-10, -10}, {10, 10}}, rotation = -90)));
  Modelica.Electrical.Analog.Ideal.IdealOpAmp3Pin opAmp annotation(
    Placement(visible = true, transformation(origin = {36, 10}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Electrical.Analog.Basic.Ground ground annotation(
    Placement(visible = true, transformation(origin = {-6, -84}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Electrical.Analog.Interfaces.Pin pin annotation(
    Placement(visible = true, transformation(origin = {12, -26}, extent = {{-6, -6}, {6, 6}}, rotation = 0), iconTransformation(origin = {12, -26}, extent = {{-6, -6}, {6, 6}}, rotation = 0)));
  Modelica.Electrical.Analog.Interfaces.Pin pin1 annotation(
    Placement(visible = true, transformation(origin = {69, 9}, extent = {{-5, -5}, {5, 5}}, rotation = 0), iconTransformation(origin = {69, 9}, extent = {{-5, -5}, {5, 5}}, rotation = 0)));
  Modelica.Electrical.Analog.Interfaces.Pin pin2 annotation(
    Placement(visible = true, transformation(origin = {-18, 16}, extent = {{-6, -6}, {6, 6}}, rotation = 0), iconTransformation(origin = {-18, 16}, extent = {{-6, -6}, {6, 6}}, rotation = 0)));
  Modelica.Electrical.Analog.Interfaces.Pin pin3 annotation(
    Placement(visible = true, transformation(origin = {-62, 16}, extent = {{-4, -4}, {4, 4}}, rotation = 0), iconTransformation(origin = {-62, 16}, extent = {{-4, -4}, {4, 4}}, rotation = 0)));
equation
  connect(opAmp.out, pin1) annotation(
    Line(points = {{46, 10}, {69, 10}, {69, 9}}, color = {0, 0, 255}));
  connect(pin1, voltageSensor.p) annotation(
    Line(points = {{69, 9}, {82, 9}, {82, -26}}, color = {0, 0, 255}));
  connect(voltageSensor.n, ground.p) annotation(
    Line(points = {{82, -46}, {82, -74}, {-6, -74}}, color = {0, 0, 255}));
  connect(sineVoltage.n, ground.p) annotation(
    Line(points = {{-94, -40}, {-94, -74}, {-6, -74}}, color = {0, 0, 255}));
  connect(R2.n, pin1) annotation(
    Line(points = {{50, -24}, {70, -24}, {70, 10}, {70, 10}}, color = {0, 0, 255}));
  connect(R2.p, pin) annotation(
    Line(points = {{30, -24}, {12, -24}, {12, -26}, {12, -26}}, color = {0, 0, 255}));
  connect(pin, opAmp.in_p) annotation(
    Line(points = {{12, -26}, {10, -26}, {10, 4}, {26, 4}, {26, 4}}, color = {0, 0, 255}));
  connect(pin, R1.n) annotation(
    Line(points = {{12, -26}, {12, -26}, {12, -40}, {12, -40}}, color = {0, 0, 255}));
  connect(R1.p, ground.p) annotation(
    Line(points = {{12, -60}, {12, -60}, {12, -74}, {-6, -74}, {-6, -74}}, color = {0, 0, 255}));
  connect(pin2, opAmp.in_n) annotation(
    Line(points = {{-18, 16}, {26, 16}}, color = {0, 0, 255}));
  connect(sineVoltage.p, R3.n) annotation(
    Line(points = {{-94, -20}, {-94, 16}, {-90, 16}}, color = {0, 0, 255}));
  connect(pin2, R4.p) annotation(
    Line(points = {{-18, 16}, {-32, 16}}, color = {0, 0, 255}));
  connect(pin2, C2.p) annotation(
    Line(points = {{-18, 16}, {-18, -22}}, color = {0, 0, 255}));
  connect(C2.n, ground.p) annotation(
    Line(points = {{-18, -42}, {-18, -74}, {-6, -74}}, color = {0, 0, 255}));
  connect(R4.n, pin3) annotation(
    Line(points = {{-52, 16}, {-64, 16}, {-64, 16}, {-62, 16}}, color = {0, 0, 255}));
  connect(pin3, R3.p) annotation(
    Line(points = {{-62, 16}, {-72, 16}, {-72, 16}, {-70, 16}}, color = {0, 0, 255}));
  connect(C1.n, pin3) annotation(
    Line(points = {{22, 50}, {-62, 50}, {-62, 16}}, color = {0, 0, 255}));
  connect(C1.p, pin1) annotation(
    Line(points = {{42, 50}, {70, 50}, {70, 8}, {70, 8}, {70, 10}}, color = {0, 0, 255}));
  annotation(
    uses(Modelica(version = "3.2.3")),
    Diagram(graphics = {Text(origin = {-48, 87}, extent = {{-22, 5}, {112, -13}}, textString = "Active Low Pass Filter Second Order", textStyle = {TextStyle.Italic, TextStyle.Italic})}));
end activelowpassSecondOrder;
