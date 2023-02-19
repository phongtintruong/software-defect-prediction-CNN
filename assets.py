from collections import OrderedDict

selection_node = ["FormalParameter","BasicType","PackageDeclaration","InterfaceDeclaration",
                  "CatchClauseParameter","ClassDeclaration","MethodInvocation","SuperMethodInvocation",
                  "MemberReference","SuperMemberReference","ConstructorDeclaration","ReferenceType",
                  "MethodDeclaration","VariableDeclarator","IfStatement","WhileStatement","DoStatement",
                  "ForStatement","AssertStatement","BreakStatement","ContinueStatement","ReturnStatement","ThrowStatement",
                  "SynchronizedStatement","TryStatement","SwitchStatement","BlockStatement","StatementExpression","TryResource",
                  "CatchClause","CatchClauseParameter","SwitchStatementCase", "ForControl", "EnhancedForControl"]

class_selec = [("<class 'javalang.tree."+ node +"'>") for node in selection_node]

token_types = OrderedDict()
for i,types in enumerate(class_selec):
  token_types[types] = i+1