const existence = {
  Location: "nvarchar, input",
  PID: "bigint, Output",
  SDY: "varchar, Output",
  PTY: "varchar, Output",
  user_token: "varchar, input"
};

const propAdd = {
  Location: "nvarchar, input",
  RecordTStamp: "datetime, input",
  HousingType: "varchar, input",
  hyperlink: "varchar, input",
  County: "varchar, input",
  SchoolDistrict: "varchar, input",
  CurrentPrice: "money, input",
  Built: "int, input",
  bed: "varchar, input",
  bath: "varchar, input",
  sqft: "varchar, input",
  lotsize: "varchar, input",
  MonthlyPmt: "money, input",
  PropertyTax: "money, input",
  Insurance: "money, input",
  HOA: "money, input",
  IMG: "blob, input",
  user_token: "varchar, input",
  PID: "bigint, output"
};

const removeAfterTest = {
  Location: "nvarchar, input",
  PID: "bigint, output"
};

const geoProp = {
  Prop_id: "bigint, input",
  Location: "varchar, input",
  RecordTStamp: "datetime, input",
  GeoResponse: "varchar, input",
  GeoAddress: "varchar, input",
  GeoCity: "varchar, input",
  GeoCounty: "varchar, input",
  GeoState: "varchar, input",
  GeoZIP: "varchar, input",
  Lat: "float, input",
  Lng: "float, input",
  Accuracy: "float, input",
  AccuracyType: "varchar, input",
  GeoSource: "varchar, input",
  USDName: "varchar, input",
  USDLEAID: "varchar, input"
};

const savedProp = {
  Prop_id: "bigint, input"
};

const addUser = {
  Location: "nvarchar, input",
  PID: "bigint, output",
  user_token: "varchar, input",
  RecordTStamp: "datetime, input"
};
