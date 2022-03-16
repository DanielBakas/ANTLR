grammar marzo;
program: (expression | statement)+;

expression:
	// COMPARISONS
	expression comparator = EQ expression	# equal
	| expression comparator = LE expression	# lessequal
	| expression comparator = LT expression	# less
	| expression comparator = ME expression	# moreequal
	| expression comparator = MT expression	# more
	// OPERATIONS
	| expression operator = ADD expression			# addition
	| expression operator = DIVIDE expression		# division
	| expression operator = MOD expression			# module
	| expression operator = MULTIPLY expression		# multiplication
	| expression operator = SUBSTRACT expression	# substraction
	| '(' expression ')'							# parenthesis
	// DATATYPES
	| INT # integer
	// VARIABLE
	| VAR # variable;

statement:
	// ASSIGNMENTS
	VAR assigner = ASSIGN expression			# assign
	| VAR assigner = ADD_ASSIGN expression		# add_assign
	| VAR assigner = DIVIDE_ASSIGN expression	# divide_assign
	| VAR assigner = MOD_ASSIGN expression		# mod_assign
	| VAR assigner = MULTIPLY_ASSIGN expression	# multiply_assign
	| VAR assigner = POWER_ASSIGN expression	# multiply_assign
	// DECLARATION
	| 'int' VAR # declare_int;

// SYMBOLS
VAR: [a-z_][A-z0-9_]+;
WS: [ \t\n\r]+ -> skip;

// DATATYPES
INT: [0-9]+;

// ASSIGNERS
ADD_ASSIGN: '+=';
ASSIGN: '=';
DIVIDE_ASSIGN: '/=';
MOD_ASSIGN: '%=';
MULTIPLY_ASSIGN: '*=';
POWER_ASSIGN: '^=';

// COMPARATORS
EQ: '==';
LE: '<=';
LT: '<';
ME: '>=';
MT: '>';

// OPERATORS
ADD: '+';
DIVIDE: '/';
MOD: '%';
MULTIPLY: '*';
POWER: '^';
SUBSTRACT: '-';