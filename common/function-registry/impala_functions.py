#!/usr/bin/env python
# Copyright 2012 Cloudera Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# This is a list of all the functions that are not auto-generated.
# It contains all the meta data that describes the function.
templated_type_symbol_map = {
  'bool'      : 'b',
  'int8_t'    : 'a',
  'int16_t'   : 's',
  'int32_t'   : 'i',
  'int64_t'   : 'l',
  'float'     : 'f',
  'double'    : 'd',
  'string'    : 'NS_11StringValueE',
  'timestamp' : 'NS_14TimestampValueE'
}

# Generates the BE symbol for the Compute Function class_name::fn_name<templated_type>.
# Does not handle varargs.
# TODO: this is a stopgap. ComputeFunctions are being removed and we can use the
# symbol lookup code in the BE.
def symbol(class_name, fn_name, templated_type = None):
  sym = '_ZN6impala'
  sym += str(len(class_name)) + class_name
  sym += str(len(fn_name)) + fn_name
  if templated_type == None:
    sym += 'EPNS_4ExprEPNS_8TupleRowE'
  else:
    sym += 'I'
    sym += templated_type_symbol_map[templated_type]
    sym += 'EEPvPNS_4ExprEPNS_8TupleRowE'
  return sym

# The format is:
#   [sql aliases], <return_type>, [<args>], <backend symbol>,
# With an optional
#   <prepare symbol>, <close symbol>
#
# 'sql aliases' are the function names that can be used from sql. There must be
# at least one per function.
#
# The symbol can be empty for functions that are not yet implemented.
functions = [
  # Math builtin functions
  [['pi'], 'DOUBLE', [], symbol('MathFunctions', 'Pi')],
  [['e'], 'DOUBLE', [], symbol('MathFunctions', 'E')],
  [['abs'], 'DOUBLE', ['DOUBLE'], symbol('MathFunctions', 'Abs')],
  [['sign'], 'FLOAT', ['DOUBLE'], symbol('MathFunctions', 'Sign')],
  [['sin'], 'DOUBLE', ['DOUBLE'], symbol('MathFunctions', 'Sin')],
  [['asin'], 'DOUBLE', ['DOUBLE'], symbol('MathFunctions', 'Asin')],
  [['cos'], 'DOUBLE', ['DOUBLE'], symbol('MathFunctions', 'Cos')],
  [['acos'], 'DOUBLE', ['DOUBLE'], symbol('MathFunctions', 'Acos')],
  [['tan'], 'DOUBLE', ['DOUBLE'], symbol('MathFunctions', 'Tan')],
  [['atan'], 'DOUBLE', ['DOUBLE'], symbol('MathFunctions', 'Atan')],
  [['radians'], 'DOUBLE', ['DOUBLE'], symbol('MathFunctions', 'Radians')],
  [['degrees'], 'DOUBLE', ['DOUBLE'], symbol('MathFunctions', 'Degrees')],
  [['ceil', 'ceiling'], 'BIGINT', ['DOUBLE'], symbol('MathFunctions', 'Ceil')],
  [['floor'], 'BIGINT', ['DOUBLE'], symbol('MathFunctions', 'Floor')],
  [['round'], 'BIGINT', ['DOUBLE'], symbol('MathFunctions', 'Round')],
  [['round'], 'DOUBLE', ['DOUBLE', 'INT'], symbol('MathFunctions', 'RoundUpTo')],
  [['exp'], 'DOUBLE', ['DOUBLE'], symbol('MathFunctions', 'Exp')],
  [['ln'], 'DOUBLE', ['DOUBLE'], symbol('MathFunctions', 'Ln')],
  [['log10'], 'DOUBLE', ['DOUBLE'], symbol('MathFunctions', 'Log10')],
  [['log2'], 'DOUBLE', ['DOUBLE'], symbol('MathFunctions', 'Log2')],
  [['log'], 'DOUBLE', ['DOUBLE', 'DOUBLE'], symbol('MathFunctions', 'Log')],
  [['pow', 'power'], 'DOUBLE', ['DOUBLE', 'DOUBLE'], symbol('MathFunctions', 'Pow')],
  [['sqrt'], 'DOUBLE', ['DOUBLE'], symbol('MathFunctions', 'Sqrt')],
  [['rand'], 'DOUBLE', [], symbol('MathFunctions', 'Rand')],
  [['rand'], 'DOUBLE', ['INT'], symbol('MathFunctions', 'RandSeed')],
  [['bin'], 'STRING', ['BIGINT'], symbol('MathFunctions', 'Bin')],
  [['hex'], 'STRING', ['BIGINT'], symbol('MathFunctions', 'HexInt')],
  [['hex'], 'STRING', ['STRING'], symbol('MathFunctions', 'HexString')],
  [['unhex'], 'STRING', ['STRING'], symbol('MathFunctions', 'Unhex')],
  [['conv'], 'STRING', ['BIGINT', 'TINYINT', 'TINYINT'],
      symbol('MathFunctions', 'ConvInt')],
  [['conv'], 'STRING', ['STRING', 'TINYINT', 'TINYINT'],
      symbol('MathFunctions', 'ConvString')],
  [['pmod'], 'BIGINT', ['BIGINT', 'BIGINT'], symbol('MathFunctions', 'PmodBigInt')],
  [['pmod'], 'DOUBLE', ['DOUBLE', 'DOUBLE'], symbol('MathFunctions', 'PmodDouble')],
  [['fmod'], 'FLOAT', ['FLOAT', 'FLOAT'], symbol('MathFunctions', 'FmodFloat')],
  [['fmod'], 'DOUBLE', ['DOUBLE', 'DOUBLE'], symbol('MathFunctions', 'FmodDouble')],
  [['positive'], 'TINYINT', ['TINYINT'],
      symbol('MathFunctions', 'Positive', 'int8_t')],
  [['positive'], 'SMALLINT', ['SMALLINT'],
      symbol('MathFunctions', 'Positive', 'int16_t')],
  [['positive'], 'INT', ['INT'],
      symbol('MathFunctions', 'Positive', 'int32_t')],
  [['positive'], 'BIGINT', ['BIGINT'],
      symbol('MathFunctions', 'Positive', 'int64_t')],
  [['positive'], 'FLOAT', ['FLOAT'],
      symbol('MathFunctions', 'Positive', 'float')],
  [['positive'], 'DOUBLE', ['DOUBLE'],
      symbol('MathFunctions', 'Positive', 'double')],
  [['negative'], 'TINYINT', ['TINYINT'],
      symbol('MathFunctions', 'Negative', 'int8_t')],
  [['negative'], 'SMALLINT', ['SMALLINT'],
      symbol('MathFunctions', 'Negative', 'int16_t')],
  [['negative'], 'INT', ['INT'],
      symbol('MathFunctions', 'Negative', 'int32_t')],
  [['negative'], 'BIGINT', ['BIGINT'],
      symbol('MathFunctions', 'Negative', 'int64_t')],
  [['negative'], 'FLOAT', ['FLOAT'],
      symbol('MathFunctions', 'Negative', 'float')],
  [['negative'], 'DOUBLE', ['DOUBLE'],
      symbol('MathFunctions', 'Negative', 'double')],
  [['quotient'], 'BIGINT', ['BIGINT', 'BIGINT'],
      symbol('MathFunctions', 'QuotientBigInt')],
  [['quotient'], 'BIGINT', ['DOUBLE', 'DOUBLE'],
      symbol('MathFunctions', 'QuotientDouble')],
  [['least'], 'TINYINT', ['TINYINT', '...'],
      '_ZN6impala13MathFunctions13LeastGreatestIaLb1EEEPvPNS_4ExprEPNS_8TupleRowE'],
  [['least'], 'SMALLINT', ['SMALLINT', '...'],
      '_ZN6impala13MathFunctions13LeastGreatestIsLb1EEEPvPNS_4ExprEPNS_8TupleRowE'],
  [['least'], 'INT', ['INT', '...'],
      '_ZN6impala13MathFunctions13LeastGreatestIiLb1EEEPvPNS_4ExprEPNS_8TupleRowE'],
  [['least'], 'BIGINT', ['BIGINT', '...'],
      '_ZN6impala13MathFunctions13LeastGreatestIlLb1EEEPvPNS_4ExprEPNS_8TupleRowE'],
  [['least'], 'FLOAT', ['FLOAT', '...'],
      '_ZN6impala13MathFunctions13LeastGreatestIfLb1EEEPvPNS_4ExprEPNS_8TupleRowE'],
  [['least'], 'DOUBLE', ['DOUBLE', '...'],
      '_ZN6impala13MathFunctions13LeastGreatestIdLb1EEEPvPNS_4ExprEPNS_8TupleRowE'],
  [['least'], 'TIMESTAMP', ['TIMESTAMP', '...'],
      '_ZN6impala13MathFunctions13LeastGreatestINS_14TimestampValueELb1EEEPvPNS_4ExprEPNS_8TupleRowE'],
  [['least'], 'STRING', ['STRING', '...'],
      '_ZN6impala13MathFunctions19LeastGreatestStringILb1EEEPvPNS_4ExprEPNS_8TupleRowE'],
  [['greatest'], 'TINYINT', ['TINYINT', '...'],
      '_ZN6impala13MathFunctions13LeastGreatestIaLb0EEEPvPNS_4ExprEPNS_8TupleRowE'],
  [['greatest'], 'SMALLINT', ['SMALLINT', '...'],
      '_ZN6impala13MathFunctions13LeastGreatestIsLb0EEEPvPNS_4ExprEPNS_8TupleRowE'],
  [['greatest'], 'INT', ['INT', '...'],
      '_ZN6impala13MathFunctions13LeastGreatestIiLb0EEEPvPNS_4ExprEPNS_8TupleRowE'],
  [['greatest'], 'BIGINT', ['BIGINT', '...'],
      '_ZN6impala13MathFunctions13LeastGreatestIlLb0EEEPvPNS_4ExprEPNS_8TupleRowE'],
  [['greatest'], 'FLOAT', ['FLOAT', '...'],
      '_ZN6impala13MathFunctions13LeastGreatestIfLb0EEEPvPNS_4ExprEPNS_8TupleRowE'],
  [['greatest'], 'DOUBLE', ['DOUBLE', '...'],
      '_ZN6impala13MathFunctions13LeastGreatestIdLb0EEEPvPNS_4ExprEPNS_8TupleRowE'],
  [['greatest'], 'TIMESTAMP', ['TIMESTAMP', '...'],
      '_ZN6impala13MathFunctions13LeastGreatestINS_14TimestampValueELb0EEEPvPNS_4ExprEPNS_8TupleRowE'],
  [['greatest'], 'STRING', ['STRING', '...'],
      '_ZN6impala13MathFunctions19LeastGreatestStringILb0EEEPvPNS_4ExprEPNS_8TupleRowE'],

  # String builtin functions
  [['substr', 'substring'], 'STRING', ['STRING', 'INT'],
      symbol('StringFunctions', 'Substring', 'int32_t')],
  [['substr', 'substring'], 'STRING', ['STRING', 'BIGINT'],
      symbol('StringFunctions', 'Substring', 'int64_t')],
  [['substr', 'substring'], 'STRING', ['STRING', 'INT', 'INT'],
      symbol('StringFunctions', 'Substring', 'int32_t')],
  [['substr', 'substring'], 'STRING', ['STRING', 'BIGINT', 'BIGINT'],
      symbol('StringFunctions', 'Substring', 'int64_t')],
# left and right are key words, leave them out for now.
  [['strleft'], 'STRING', ['STRING', 'INT'],
      symbol('StringFunctions', 'Left', 'int32_t')],
  [['strleft'], 'STRING', ['STRING', 'BIGINT'],
      symbol('StringFunctions', 'Left', 'int64_t')],
  [['strright'], 'STRING', ['STRING', 'INT'],
      symbol('StringFunctions', 'Right', 'int32_t')],
  [['strright'], 'STRING', ['STRING', 'BIGINT'],
      symbol('StringFunctions', 'Right', 'int64_t')],
  [['space'], 'STRING', ['INT'], symbol('StringFunctions', 'Space', 'int32_t')],
  [['space'], 'STRING', ['BIGINT'], symbol('StringFunctions', 'Space', 'int64_t')],
  [['repeat'], 'STRING', ['STRING', 'INT'],
      symbol('StringFunctions', 'Repeat', 'int32_t')],
  [['repeat'], 'STRING', ['STRING', 'BIGINT'],
      symbol('StringFunctions', 'Repeat', 'int64_t')],
  [['lpad'], 'STRING', ['STRING', 'INT', 'STRING'],
      symbol('StringFunctions', 'Lpad', 'int32_t')],
  [['lpad'], 'STRING', ['STRING', 'BIGINT', 'STRING'],
      symbol('StringFunctions', 'Lpad', 'int64_t')],
  [['rpad'], 'STRING', ['STRING', 'INT', 'STRING'],
      symbol('StringFunctions', 'Rpad', 'int32_t')],
  [['rpad'], 'STRING', ['STRING', 'BIGINT', 'STRING'],
      symbol('StringFunctions', 'Rpad', 'int64_t')],
  [['length'], 'INT', ['STRING'], symbol('StringFunctions', 'Length')],
  [['char_length'], 'INT', ['STRING'], symbol('StringFunctions', 'Length')],
  [['character_length'], 'INT', ['STRING'], symbol('StringFunctions', 'Length')],
  [['lower', 'lcase'], 'STRING', ['STRING'], symbol('StringFunctions', 'Lower')],
  [['upper', 'ucase'], 'STRING', ['STRING'], symbol('StringFunctions', 'Upper')],
  [['initcap'], 'STRING', ['STRING'], symbol('StringFunctions', 'InitCap')],
  [['reverse'], 'STRING', ['STRING'], symbol('StringFunctions', 'Reverse')],
  [['translate'], 'STRING', ['STRING', 'STRING', 'STRING'],
      symbol('StringFunctions', 'Translate')],
  [['trim'], 'STRING', ['STRING'], symbol('StringFunctions', 'Trim')],
  [['ltrim'], 'STRING', ['STRING'], symbol('StringFunctions', 'Ltrim')],
  [['rtrim'], 'STRING', ['STRING'], symbol('StringFunctions', 'Rtrim')],
  [['ascii'], 'INT', ['STRING'], symbol('StringFunctions', 'Ascii')],
  [['instr'], 'INT', ['STRING', 'STRING'], symbol('StringFunctions', 'Instr')],
  [['locate'], 'INT', ['STRING', 'STRING'], symbol('StringFunctions', 'Locate')],
  [['locate'], 'INT', ['STRING', 'STRING', 'INT'],
      symbol('StringFunctions', 'LocatePos', 'int32_t')],
  [['locate'], 'INT', ['STRING', 'STRING', 'BIGINT'],
      symbol('StringFunctions', 'LocatePos', 'int64_t')],
  [['regexp_extract'], 'STRING', ['STRING', 'STRING', 'INT'],
      symbol('StringFunctions', 'RegexpExtract', 'int32_t')],
  [['regexp_extract'], 'STRING', ['STRING', 'STRING', 'BIGINT'],
      symbol('StringFunctions', 'RegexpExtract', 'int64_t')],
  [['regexp_replace'], 'STRING', ['STRING', 'STRING', 'STRING'],
      symbol('StringFunctions', 'RegexpReplace')],
  [['concat'], 'STRING', ['STRING', '...'], symbol('StringFunctions', 'Concat')],
  [['concat_ws'], 'STRING', ['STRING', 'STRING', '...'],
      symbol('StringFunctions', 'ConcatWs')],
  [['find_in_set'], 'INT', ['STRING', 'STRING'], symbol('StringFunctions', 'FindInSet')],
  [['parse_url'], 'STRING', ['STRING', 'STRING'], symbol('StringFunctions', 'ParseUrl')],
  [['parse_url'], 'STRING', ['STRING', 'STRING', 'STRING'],
      symbol('StringFunctions', 'ParseUrlKey')],

  # Utility functions
  [['current_database'], 'STRING', [], symbol('UtilityFunctions', 'CurrentDatabase')],
  [['user'], 'STRING', [], symbol('UtilityFunctions', 'User')],
  [['sleep'], 'BOOLEAN', ['INT'], symbol('UtilityFunctions', 'Sleep')],
  [['pid'], 'INT', [], symbol('UtilityFunctions', 'Pid')],
  [['version'], 'STRING', [], symbol('UtilityFunctions', 'Version')],

  [['fnv_hash'], 'BIGINT', ['TINYINT'],
      '_ZN6impala16UtilityFunctions7FnvHashILi1EEEPvPNS_4ExprEPNS_8TupleRowE'],
  [['fnv_hash'], 'BIGINT', ['SMALLINT'],
      '_ZN6impala16UtilityFunctions7FnvHashILi2EEEPvPNS_4ExprEPNS_8TupleRowE'],
  [['fnv_hash'], 'BIGINT', ['INT'],
      '_ZN6impala16UtilityFunctions7FnvHashILi4EEEPvPNS_4ExprEPNS_8TupleRowE'],
  [['fnv_hash'], 'BIGINT', ['BIGINT'],
      '_ZN6impala16UtilityFunctions7FnvHashILi8EEEPvPNS_4ExprEPNS_8TupleRowE'],
  [['fnv_hash'], 'BIGINT', ['FLOAT'],
      '_ZN6impala16UtilityFunctions7FnvHashILi4EEEPvPNS_4ExprEPNS_8TupleRowE'],
  [['fnv_hash'], 'BIGINT', ['DOUBLE'],
      '_ZN6impala16UtilityFunctions7FnvHashILi8EEEPvPNS_4ExprEPNS_8TupleRowE'],
  [['fnv_hash'], 'BIGINT', ['TIMESTAMP'],
      '_ZN6impala16UtilityFunctions7FnvHashILi12EEEPvPNS_4ExprEPNS_8TupleRowE'],
  [['fnv_hash'], 'BIGINT', ['STRING'],
      '_ZN6impala16UtilityFunctions13FnvHashStringEPNS_4ExprEPNS_8TupleRowE'],

  # Timestamp Functions
  [['unix_timestamp'], 'INT', [], symbol('TimestampFunctions', 'Unix')],
  [['unix_timestamp'], 'INT', ['STRING'], symbol('TimestampFunctions', 'UnixFromString')],
  [['unix_timestamp'], 'INT', ['TIMESTAMP'], symbol('TimestampFunctions', 'Unix')],
  [['unix_timestamp'], 'INT', ['STRING', 'STRING'], symbol('TimestampFunctions', 'Unix')],
  [['from_unixtime'], 'STRING', ['INT'],
      symbol('TimestampFunctions', 'FromUnix', 'int32_t')],
  [['from_unixtime'], 'STRING', ['INT', 'STRING'],
      symbol('TimestampFunctions', 'FromUnix', 'int32_t')],
  [['from_unixtime'], 'STRING', ['BIGINT'],
      symbol('TimestampFunctions', 'FromUnix', 'int64_t')],
  [['from_unixtime'], 'STRING', ['BIGINT', 'STRING'],
      symbol('TimestampFunctions', 'FromUnix', 'int64_t')],
  [['dayname'], 'STRING', ['TIMESTAMP'], symbol('TimestampFunctions', 'DayName')],
  [['year'], 'INT', ['TIMESTAMP'], symbol('TimestampFunctions', 'Year')],
  [['month'], 'INT', ['TIMESTAMP'], symbol('TimestampFunctions', 'Month')],
  [['day', 'dayofmonth'], 'INT', ['TIMESTAMP'],
      symbol('TimestampFunctions', 'DayOfMonth')],
  [['dayofweek'], 'INT', ['TIMESTAMP'], symbol('TimestampFunctions', 'DayOfWeek')],
  [['dayofyear'], 'INT', ['TIMESTAMP'], symbol('TimestampFunctions', 'DayOfYear')],
  [['weekofyear'], 'INT', ['TIMESTAMP'], symbol('TimestampFunctions', 'WeekOfYear')],
  [['hour'], 'INT', ['TIMESTAMP'], symbol('TimestampFunctions', 'Hour')],
  [['minute'], 'INT', ['TIMESTAMP'], symbol('TimestampFunctions', 'Minute')],
  [['second'], 'INT', ['TIMESTAMP'], symbol('TimestampFunctions', 'Second')],
  [['now', 'current_timestamp'], 'TIMESTAMP', [], symbol('TimestampFunctions', 'Now')],
  [['to_date'], 'STRING', ['TIMESTAMP'], symbol('TimestampFunctions', 'ToDate')],
  [['datediff'], 'INT', ['TIMESTAMP', 'TIMESTAMP'],
      symbol('TimestampFunctions', 'DateDiff')],
  [['from_utc_timestamp'], 'TIMESTAMP', ['TIMESTAMP', 'STRING'],
      symbol('TimestampFunctions', 'FromUtc')],
  [['to_utc_timestamp'], 'TIMESTAMP', ['TIMESTAMP', 'STRING'],
      symbol('TimestampFunctions', 'ToUtc')],

  # Date and time add/sub functions.
  # TODO: there must be a better way to deal with this symbols.
  [['years_add'], 'TIMESTAMP', ['TIMESTAMP', 'INT'],
      '_ZN6impala18TimestampFunctions10DateAddSubILb1EiN5boost9date_time14years_durationINS2_9gregorian21greg_durations_configEEEEEPvPNS_4ExprEPNS_8TupleRowE'],
  [['years_add'], 'TIMESTAMP', ['TIMESTAMP', 'BIGINT'],
      '_ZN6impala18TimestampFunctions10DateAddSubILb1ElN5boost9date_time14years_durationINS2_9gregorian21greg_durations_configEEEEEPvPNS_4ExprEPNS_8TupleRowE'],
  [['years_sub'], 'TIMESTAMP', ['TIMESTAMP', 'INT'],
      '_ZN6impala18TimestampFunctions10DateAddSubILb0EiN5boost9date_time14years_durationINS2_9gregorian21greg_durations_configEEEEEPvPNS_4ExprEPNS_8TupleRowE'],
  [['years_sub'], 'TIMESTAMP', ['TIMESTAMP', 'BIGINT'],
      '_ZN6impala18TimestampFunctions10DateAddSubILb0ElN5boost9date_time14years_durationINS2_9gregorian21greg_durations_configEEEEEPvPNS_4ExprEPNS_8TupleRowE'],
  [['months_add', 'add_months'], 'TIMESTAMP', ['TIMESTAMP', 'INT'],
      '_ZN6impala18TimestampFunctions10DateAddSubILb1EiN5boost9date_time15months_durationINS2_9gregorian21greg_durations_configEEEEEPvPNS_4ExprEPNS_8TupleRowE'],
  [['months_add', 'add_months'], 'TIMESTAMP', ['TIMESTAMP', 'BIGINT'],
      '_ZN6impala18TimestampFunctions10DateAddSubILb1ElN5boost9date_time15months_durationINS2_9gregorian21greg_durations_configEEEEEPvPNS_4ExprEPNS_8TupleRowE'],
  [['months_sub'], 'TIMESTAMP', ['TIMESTAMP', 'INT'],
      '_ZN6impala18TimestampFunctions10DateAddSubILb0EiN5boost9date_time15months_durationINS2_9gregorian21greg_durations_configEEEEEPvPNS_4ExprEPNS_8TupleRowE'],
  [['months_sub'], 'TIMESTAMP', ['TIMESTAMP', 'BIGINT'],
      '_ZN6impala18TimestampFunctions10DateAddSubILb0ElN5boost9date_time15months_durationINS2_9gregorian21greg_durations_configEEEEEPvPNS_4ExprEPNS_8TupleRowE'],
  [['weeks_add'], 'TIMESTAMP', ['TIMESTAMP', 'INT'],
      '_ZN6impala18TimestampFunctions10DateAddSubILb1EiN5boost9gregorian14weeks_durationEEEPvPNS_4ExprEPNS_8TupleRowE'],
  [['weeks_add'], 'TIMESTAMP', ['TIMESTAMP', 'BIGINT'],
      '_ZN6impala18TimestampFunctions10DateAddSubILb1ElN5boost9gregorian14weeks_durationEEEPvPNS_4ExprEPNS_8TupleRowE'],
  [['weeks_sub'], 'TIMESTAMP', ['TIMESTAMP', 'INT'],
      '_ZN6impala18TimestampFunctions10DateAddSubILb0EiN5boost9gregorian14weeks_durationEEEPvPNS_4ExprEPNS_8TupleRowE'],
  [['weeks_sub'], 'TIMESTAMP', ['TIMESTAMP', 'BIGINT'],
      '_ZN6impala18TimestampFunctions10DateAddSubILb0ElN5boost9gregorian14weeks_durationEEEPvPNS_4ExprEPNS_8TupleRowE'],
  [['days_add', 'date_add', 'adddate'], 'TIMESTAMP', ['TIMESTAMP', 'INT'],
      '_ZN6impala18TimestampFunctions10DateAddSubILb1EiN5boost9gregorian13date_durationEEEPvPNS_4ExprEPNS_8TupleRowE'],
  [['days_add', 'date_add', 'adddate'], 'TIMESTAMP', ['TIMESTAMP', 'BIGINT'],
      '_ZN6impala18TimestampFunctions10DateAddSubILb1ElN5boost9gregorian13date_durationEEEPvPNS_4ExprEPNS_8TupleRowE'],
  [['days_sub', 'date_sub', 'subdate'], 'TIMESTAMP', ['TIMESTAMP', 'INT'],
      '_ZN6impala18TimestampFunctions10DateAddSubILb0EiN5boost9gregorian13date_durationEEEPvPNS_4ExprEPNS_8TupleRowE'],
  [['days_sub', 'date_sub', 'subdate'], 'TIMESTAMP', ['TIMESTAMP', 'BIGINT'],
      '_ZN6impala18TimestampFunctions10DateAddSubILb0ElN5boost9gregorian13date_durationEEEPvPNS_4ExprEPNS_8TupleRowE'],
  [['hours_add'], 'TIMESTAMP', ['TIMESTAMP', 'INT'],
      '_ZN6impala18TimestampFunctions10TimeAddSubILb1EiN5boost10posix_time5hoursEEEPvPNS_4ExprEPNS_8TupleRowE'],
  [['hours_add'], 'TIMESTAMP', ['TIMESTAMP', 'BIGINT'],
      '_ZN6impala18TimestampFunctions10TimeAddSubILb1ElN5boost10posix_time5hoursEEEPvPNS_4ExprEPNS_8TupleRowE'],
  [['hours_sub'], 'TIMESTAMP', ['TIMESTAMP', 'INT'],
      '_ZN6impala18TimestampFunctions10TimeAddSubILb0EiN5boost10posix_time5hoursEEEPvPNS_4ExprEPNS_8TupleRowE'],
  [['hours_sub'], 'TIMESTAMP', ['TIMESTAMP', 'BIGINT'],
      '_ZN6impala18TimestampFunctions10TimeAddSubILb0ElN5boost10posix_time5hoursEEEPvPNS_4ExprEPNS_8TupleRowE'],
  [['minutes_add'], 'TIMESTAMP', ['TIMESTAMP', 'INT'],
      '_ZN6impala18TimestampFunctions10TimeAddSubILb1EiN5boost10posix_time7minutesEEEPvPNS_4ExprEPNS_8TupleRowE'],
  [['minutes_add'], 'TIMESTAMP', ['TIMESTAMP', 'BIGINT'],
      '_ZN6impala18TimestampFunctions10TimeAddSubILb1ElN5boost10posix_time7minutesEEEPvPNS_4ExprEPNS_8TupleRowE'],
  [['minutes_sub'], 'TIMESTAMP', ['TIMESTAMP', 'INT'],
      '_ZN6impala18TimestampFunctions10TimeAddSubILb0EiN5boost10posix_time7minutesEEEPvPNS_4ExprEPNS_8TupleRowE'],
  [['minutes_sub'], 'TIMESTAMP', ['TIMESTAMP', 'BIGINT'],
      '_ZN6impala18TimestampFunctions10TimeAddSubILb0ElN5boost10posix_time7minutesEEEPvPNS_4ExprEPNS_8TupleRowE'],
  [['seconds_add'], 'TIMESTAMP', ['TIMESTAMP', 'INT'],
      '_ZN6impala18TimestampFunctions10TimeAddSubILb1EiN5boost10posix_time7secondsEEEPvPNS_4ExprEPNS_8TupleRowE'],
  [['seconds_add'], 'TIMESTAMP', ['TIMESTAMP', 'BIGINT'],
      '_ZN6impala18TimestampFunctions10TimeAddSubILb1ElN5boost10posix_time7secondsEEEPvPNS_4ExprEPNS_8TupleRowE'],
  [['seconds_sub'], 'TIMESTAMP', ['TIMESTAMP', 'INT'],
      '_ZN6impala18TimestampFunctions10TimeAddSubILb0EiN5boost10posix_time7secondsEEEPvPNS_4ExprEPNS_8TupleRowE'],
  [['seconds_sub'], 'TIMESTAMP', ['TIMESTAMP', 'BIGINT'],
      '_ZN6impala18TimestampFunctions10TimeAddSubILb0ElN5boost10posix_time7secondsEEEPvPNS_4ExprEPNS_8TupleRowE'],
  [['milliseconds_add'], 'TIMESTAMP', ['TIMESTAMP', 'INT'],
      '_ZN6impala18TimestampFunctions10TimeAddSubILb1EiN5boost9date_time18subsecond_durationINS2_10posix_time13time_durationELl1000EEEEEPvPNS_4ExprEPNS_8TupleRowE'],
  [['milliseconds_add'], 'TIMESTAMP', ['TIMESTAMP', 'BIGINT'],
      '_ZN6impala18TimestampFunctions10TimeAddSubILb1ElN5boost9date_time18subsecond_durationINS2_10posix_time13time_durationELl1000EEEEEPvPNS_4ExprEPNS_8TupleRowE'],
  [['milliseconds_sub'], 'TIMESTAMP', ['TIMESTAMP', 'INT'],
      '_ZN6impala18TimestampFunctions10TimeAddSubILb0EiN5boost9date_time18subsecond_durationINS2_10posix_time13time_durationELl1000EEEEEPvPNS_4ExprEPNS_8TupleRowE'],
  [['milliseconds_sub'], 'TIMESTAMP', ['TIMESTAMP', 'BIGINT'],
      '_ZN6impala18TimestampFunctions10TimeAddSubILb0ElN5boost9date_time18subsecond_durationINS2_10posix_time13time_durationELl1000EEEEEPvPNS_4ExprEPNS_8TupleRowE'],

  [['microseconds_add'], 'TIMESTAMP', ['TIMESTAMP', 'INT'],
      '_ZN6impala18TimestampFunctions10TimeAddSubILb1EiN5boost9date_time18subsecond_durationINS2_10posix_time13time_durationELl1000000EEEEEPvPNS_4ExprEPNS_8TupleRowE'],
  [['microseconds_add'], 'TIMESTAMP', ['TIMESTAMP', 'BIGINT'],
      '_ZN6impala18TimestampFunctions10TimeAddSubILb1ElN5boost9date_time18subsecond_durationINS2_10posix_time13time_durationELl1000000EEEEEPvPNS_4ExprEPNS_8TupleRowE'],
  [['microseconds_sub'], 'TIMESTAMP', ['TIMESTAMP', 'INT'],
      '_ZN6impala18TimestampFunctions10TimeAddSubILb0EiN5boost9date_time18subsecond_durationINS2_10posix_time13time_durationELl1000000EEEEEPvPNS_4ExprEPNS_8TupleRowE'],
  [['microseconds_sub'], 'TIMESTAMP', ['TIMESTAMP', 'BIGINT'],
      '_ZN6impala18TimestampFunctions10TimeAddSubILb0ElN5boost9date_time18subsecond_durationINS2_10posix_time13time_durationELl1000000EEEEEPvPNS_4ExprEPNS_8TupleRowE'],

  [['nanoseconds_add'], 'TIMESTAMP', ['TIMESTAMP', 'INT'],
      '_ZN6impala18TimestampFunctions10TimeAddSubILb1EiN5boost9date_time18subsecond_durationINS2_10posix_time13time_durationELl1000000000EEEEEPvPNS_4ExprEPNS_8TupleRowE'],
  [['nanoseconds_add'], 'TIMESTAMP', ['TIMESTAMP', 'BIGINT'],
      '_ZN6impala18TimestampFunctions10TimeAddSubILb1ElN5boost9date_time18subsecond_durationINS2_10posix_time13time_durationELl1000000000EEEEEPvPNS_4ExprEPNS_8TupleRowE'],
  [['nanoseconds_sub'], 'TIMESTAMP', ['TIMESTAMP', 'INT'],
      '_ZN6impala18TimestampFunctions10TimeAddSubILb0EiN5boost9date_time18subsecond_durationINS2_10posix_time13time_durationELl1000000000EEEEEPvPNS_4ExprEPNS_8TupleRowE'],
  [['nanoseconds_sub'], 'TIMESTAMP', ['TIMESTAMP', 'BIGINT'],
      '_ZN6impala18TimestampFunctions10TimeAddSubILb0ElN5boost9date_time18subsecond_durationINS2_10posix_time13time_durationELl1000000000EEEEEPvPNS_4ExprEPNS_8TupleRowE'],

  # Conditional Functions
  [['if'], 'BOOLEAN', ['BOOLEAN', 'BOOLEAN', 'BOOLEAN'],
      symbol('ConditionalFunctions', 'IfFn', 'bool')],
  [['if'], 'TINYINT', ['BOOLEAN', 'TINYINT', 'TINYINT'],
      symbol('ConditionalFunctions', 'IfFn', 'int8_t')],
  [['if'], 'SMALLINT', ['BOOLEAN', 'SMALLINT', 'SMALLINT'],
      symbol('ConditionalFunctions', 'IfFn', 'int16_t')],
  [['if'], 'INT', ['BOOLEAN', 'INT', 'INT'],
      symbol('ConditionalFunctions', 'IfFn', 'int32_t')],
  [['if'], 'BIGINT', ['BOOLEAN', 'BIGINT', 'BIGINT'],
      symbol('ConditionalFunctions', 'IfFn', 'int64_t')],
  [['if'], 'FLOAT', ['BOOLEAN', 'FLOAT', 'FLOAT'],
      symbol('ConditionalFunctions', 'IfFn', 'float')],
  [['if'], 'DOUBLE', ['BOOLEAN', 'DOUBLE', 'DOUBLE'],
      symbol('ConditionalFunctions', 'IfFn', 'double')],
  [['if'], 'STRING', ['BOOLEAN', 'STRING', 'STRING'],
      symbol('ConditionalFunctions', 'IfFn', 'string')],
  [['if'], 'TIMESTAMP', ['BOOLEAN', 'TIMESTAMP', 'TIMESTAMP'],
      symbol('ConditionalFunctions', 'IfFn', 'timestamp')],

  [['nullif'], 'BOOLEAN', ['BOOLEAN', 'BOOLEAN'],
      symbol('ConditionalFunctions', 'NullIf', 'bool')],
  [['nullif'], 'TINYINT', ['TINYINT', 'TINYINT'],
      symbol('ConditionalFunctions', 'NullIf', 'int8_t')],
  [['nullif'], 'SMALLINT', ['SMALLINT', 'SMALLINT'],
      symbol('ConditionalFunctions', 'NullIf', 'int16_t')],
  [['nullif'], 'INT', ['INT', 'INT'],
      symbol('ConditionalFunctions', 'NullIf', 'int32_t')],
  [['nullif'], 'BIGINT', ['BIGINT', 'BIGINT'],
      symbol('ConditionalFunctions', 'NullIf', 'int64_t')],
  [['nullif'], 'FLOAT', ['FLOAT', 'FLOAT'],
      symbol('ConditionalFunctions', 'NullIf', 'float')],
  [['nullif'], 'DOUBLE', ['DOUBLE', 'DOUBLE'],
      symbol('ConditionalFunctions', 'NullIf', 'double')],
  [['nullif'], 'STRING', ['STRING', 'STRING'],
      symbol('ConditionalFunctions', 'NullIf', 'string')],
  [['nullif'], 'TIMESTAMP', ['TIMESTAMP', 'TIMESTAMP'],
      symbol('ConditionalFunctions', 'NullIf', 'timestamp')],

  [['zeroifnull'], 'TINYINT', ['TINYINT'],
      symbol('ConditionalFunctions', 'ZeroIfNull', 'int8_t')],
  [['zeroifnull'], 'SMALLINT', ['SMALLINT'],
      symbol('ConditionalFunctions', 'ZeroIfNull', 'int16_t')],
  [['zeroifnull'], 'INT', ['INT'],
      symbol('ConditionalFunctions', 'ZeroIfNull', 'int32_t')],
  [['zeroifnull'], 'BIGINT', ['BIGINT'],
      symbol('ConditionalFunctions', 'ZeroIfNull', 'int64_t')],
  [['zeroifnull'], 'FLOAT', ['FLOAT'],
      symbol('ConditionalFunctions', 'ZeroIfNull', 'float')],
  [['zeroifnull'], 'DOUBLE', ['DOUBLE'],
      symbol('ConditionalFunctions', 'ZeroIfNull', 'double')],

  [['nullifzero'], 'TINYINT', ['TINYINT'],
      symbol('ConditionalFunctions', 'NullIfZero', 'int8_t')],
  [['nullifzero'], 'SMALLINT', ['SMALLINT'],
      symbol('ConditionalFunctions', 'NullIfZero', 'int16_t')],
  [['nullifzero'], 'INT', ['INT'],
      symbol('ConditionalFunctions', 'NullIfZero', 'int32_t')],
  [['nullifzero'], 'BIGINT', ['BIGINT'],
      symbol('ConditionalFunctions', 'NullIfZero', 'int64_t')],
  [['nullifzero'], 'FLOAT', ['FLOAT'],
      symbol('ConditionalFunctions', 'NullIfZero', 'float')],
  [['nullifzero'], 'DOUBLE', ['DOUBLE'],
      symbol('ConditionalFunctions', 'NullIfZero', 'double')],

  [['isnull', 'ifnull', 'nvl'], 'BOOLEAN', ['BOOLEAN', 'BOOLEAN'],
      symbol('ConditionalFunctions', 'IsNull')],
  [['isnull', 'ifnull', 'nvl'], 'TINYINT', ['TINYINT', 'TINYINT'],
      symbol('ConditionalFunctions', 'IsNull')],
  [['isnull', 'ifnull', 'nvl'], 'SMALLINT', ['SMALLINT', 'SMALLINT'],
      symbol('ConditionalFunctions', 'IsNull')],
  [['isnull', 'ifnull', 'nvl'], 'INT', ['INT', 'INT'],
      symbol('ConditionalFunctions', 'IsNull')],
  [['isnull', 'ifnull', 'nvl'], 'BIGINT', ['BIGINT', 'BIGINT'],
      symbol('ConditionalFunctions', 'IsNull')],
  [['isnull', 'ifnull', 'nvl'], 'FLOAT', ['FLOAT', 'FLOAT'],
      symbol('ConditionalFunctions', 'IsNull')],
  [['isnull', 'ifnull', 'nvl'], 'DOUBLE', ['DOUBLE', 'DOUBLE'],
      symbol('ConditionalFunctions', 'IsNull')],
  [['isnull', 'ifnull', 'nvl'], 'STRING', ['STRING', 'STRING'],
      symbol('ConditionalFunctions', 'IsNull')],
  [['isnull', 'ifnull', 'nvl'], 'TIMESTAMP', ['TIMESTAMP', 'TIMESTAMP'],
      symbol('ConditionalFunctions', 'IsNull')],

  [['coalesce'], 'BOOLEAN', ['BOOLEAN', '...'],
      '_ZN6impala20ConditionalFunctions8CoalesceIbEEPvPNS_4ExprEPNS_8TupleRowE'],
  [['coalesce'], 'TINYINT', ['TINYINT', '...'],
      '_ZN6impala20ConditionalFunctions8CoalesceIaEEPvPNS_4ExprEPNS_8TupleRowE'],
  [['coalesce'], 'SMALLINT', ['SMALLINT', '...'],
      '_ZN6impala20ConditionalFunctions8CoalesceIsEEPvPNS_4ExprEPNS_8TupleRowE'],
  [['coalesce'], 'INT', ['INT', '...'],
      '_ZN6impala20ConditionalFunctions8CoalesceIiEEPvPNS_4ExprEPNS_8TupleRowE'],
  [['coalesce'], 'BIGINT', ['BIGINT', '...'],
      '_ZN6impala20ConditionalFunctions8CoalesceIlEEPvPNS_4ExprEPNS_8TupleRowE'],
  [['coalesce'], 'FLOAT', ['FLOAT', '...'],
      '_ZN6impala20ConditionalFunctions8CoalesceIfEEPvPNS_4ExprEPNS_8TupleRowE'],
  [['coalesce'], 'DOUBLE', ['DOUBLE', '...'],
      '_ZN6impala20ConditionalFunctions8CoalesceIdEEPvPNS_4ExprEPNS_8TupleRowE'],
  [['coalesce'], 'STRING', ['STRING', '...'],
      '_ZN6impala20ConditionalFunctions8CoalesceINS_11StringValueEEEPvPNS_4ExprEPNS_8TupleRowE'],
  [['coalesce'], 'TIMESTAMP', ['TIMESTAMP', '...'],
      '_ZN6impala20ConditionalFunctions8CoalesceINS_14TimestampValueEEEPvPNS_4ExprEPNS_8TupleRowE'],

  # Decimal Functions
  # TODO: oracle has decimal support for transcendental functions (e.g. sin()) to very
  # high precisions. Do we need them? It's unclear if other databases do the same.
  [['precision'], 'INT', ['DECIMAL'], symbol('DecimalFunctions', 'Precision')],
  [['scale'], 'INT', ['DECIMAL'], symbol('DecimalFunctions', 'Scale')],
  [['abs'], 'DECIMAL', ['DECIMAL'], symbol('DecimalFunctions', 'Abs')],
  [['ceil', 'ceiling'], 'DECIMAL', ['DECIMAL'], symbol('DecimalFunctions', 'Ceil')],
  [['floor'], 'DECIMAL', ['DECIMAL'], symbol('DecimalFunctions', 'Floor')],
  [['round'], 'DECIMAL', ['DECIMAL'], symbol('DecimalFunctions', 'Round')],
  [['round'], 'DECIMAL', ['DECIMAL', 'INT'], symbol('DecimalFunctions', 'RoundTo')],
  [['truncate'], 'DECIMAL', ['DECIMAL'], symbol('DecimalFunctions', 'Truncate')],
  [['truncate'], 'DECIMAL', ['DECIMAL', 'INT'], symbol('DecimalFunctions', 'TruncateTo')],
]

# These functions are implemented against the UDF interface.
# TODO: this list should subsume the one above when all builtins are migrated.
udf_functions = [
  [['udf_pi'], 'DOUBLE', [],
   '_ZN6impala11UdfBuiltins2PiEPN10impala_udf15FunctionContextE'],
  [['udf_abs'], 'DOUBLE', ['DOUBLE'],
   '_ZN6impala11UdfBuiltins3AbsEPN10impala_udf15FunctionContextERKNS1_9DoubleValE'],
  [['udf_lower'], 'STRING', ['STRING'],
   '_ZN6impala11UdfBuiltins5LowerEPN10impala_udf15FunctionContextERKNS1_9StringValE'],
  [['max_int'], 'INT', [],
   '_ZN6impala11UdfBuiltins6MaxIntEPN10impala_udf15FunctionContextE'],
  [['max_tinyint'], 'TINYINT', [],
   '_ZN6impala11UdfBuiltins10MaxTinyIntEPN10impala_udf15FunctionContextE'],
  [['max_smallint'], 'SMALLINT', [],
   '_ZN6impala11UdfBuiltins11MaxSmallIntEPN10impala_udf15FunctionContextE'],
  [['max_bigint'], 'BIGINT', [],
   '_ZN6impala11UdfBuiltins9MaxBigIntEPN10impala_udf15FunctionContextE'],
  [['min_int'], 'INT', [],
   '_ZN6impala11UdfBuiltins6MinIntEPN10impala_udf15FunctionContextE'],
  [['min_tinyint'], 'TINYINT', [],
   '_ZN6impala11UdfBuiltins10MinTinyIntEPN10impala_udf15FunctionContextE'],
  [['min_smallint'], 'SMALLINT', [],
   '_ZN6impala11UdfBuiltins11MinSmallIntEPN10impala_udf15FunctionContextE'],
  [['min_bigint'], 'BIGINT', [],
   '_ZN6impala11UdfBuiltins9MinBigIntEPN10impala_udf15FunctionContextE'],
  [['is_nan'], 'BOOLEAN', ['DOUBLE'],
   '_ZN6impala11UdfBuiltins5IsNanEPN10impala_udf15FunctionContextERKNS1_9DoubleValE'],
  [['is_inf'], 'BOOLEAN', ['DOUBLE'],
   '_ZN6impala11UdfBuiltins5IsInfEPN10impala_udf15FunctionContextERKNS1_9DoubleValE'],
  [['trunc'], 'TIMESTAMP', ['TIMESTAMP', 'STRING'],
   '_ZN6impala11UdfBuiltins5TruncEPN10impala_udf15FunctionContextERKNS1_12TimestampValERKNS1_9StringValE',
   '_ZN6impala11UdfBuiltins12TruncPrepareEPN10impala_udf15FunctionContextENS2_18FunctionStateScopeE',
   '_ZN6impala11UdfBuiltins10TruncCloseEPN10impala_udf15FunctionContextENS2_18FunctionStateScopeE'],
  [['extract'], 'INT', ['TIMESTAMP', 'STRING'],
   '_ZN6impala11UdfBuiltins7ExtractEPN10impala_udf15FunctionContextERKNS1_12TimestampValERKNS1_9StringValE',
   '_ZN6impala11UdfBuiltins14ExtractPrepareEPN10impala_udf15FunctionContextENS2_18FunctionStateScopeE',
   '_ZN6impala11UdfBuiltins12ExtractCloseEPN10impala_udf15FunctionContextENS2_18FunctionStateScopeE'],
]
