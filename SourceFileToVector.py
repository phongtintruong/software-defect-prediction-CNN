import glob
import os.path
from collections import OrderedDict

import javalang
import pygments
import xmltodict
from pygments.lexers import JavaLexer
from pygments.token import Token

import pandas as pd
import csv
import numpy as np

from assets import *
from datasets import *

class ProjectVersion:
  __slots__ = ['name', 'version', 'src_files']

  def __init__(self,name,version):
    self.name = name
    self.version = version
    self.src_files = OrderedDict()


class SourceFile:
  __slots__ = ['path_file','version' , 'interVector', 'tradFeature', 'label', 'tradgene']

  def __init__ (self,path_file):
    self.path_file = path_file
    self.version = None
    self.interVector = None
    self.tradFeature = None
    self.label = None
    self.tradgene = None



class Parser():
  "class containing different parsers"
  __slots__ = ['name', 'root', 'versions', 'src', 'mapdata', 'labeldata']

  def __init__ (self, project):
    self.name = project.name
    self.root = project.root
    self.versions = project.versions
    self.src = project.src
    self.mapdata = project.mapdata
    self.labeldata = project.labeldata

  def Parser(self):
    Project = OrderedDict()
    for version in self.versions:
      Project[version] = ProjectVersion(self.name,version)

    vocab = []
    maxlen = 0
    #build vocab for all version
    for version in self.mapdata:
      with open(str(version), 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        reader.__next__()
        for line in reader:
          #get path_file of each file
          path_file =os.path.normpath((str(self.root) + line[0][27:-24]).replace("\\","/"))
          with open(path_file, encoding='cp1256') as file:
            src = file.read()
          parser_tree = None
          try:
            parser_tree = javalang.parse.parse(src)
            for path, node in parser_tree:
              if (str(type(node)) in class_selec):
                if node.name not in vocab:
                  vocab.append(node.name)
          except:
            pass



    # read each version in project
    for version, versionmap, versionlabel in zip(self.versions, self.mapdata, self.labeldata):
      print(version)
      print(versionmap)
      print(versionlabel)

      token_matrix = []
      with open(str(versionmap), 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        reader.__next__()
        for line in reader:
          #get path_file of each file
          path_file =os.path.normpath((str(self.root) + line[0][27:-24]).replace("\\","/"))
          with open(path_file, encoding='cp1256') as file:
            src = file.read()
          token_vector = []
          parser_tree = None
          try:
            parser_tree = javalang.parse.parse(src)
            for path, node in parser_tree:
              if (str(type(node)) in class_selec):
                token_vector.append(node.name)
          except:
            pass

          # Get the package declaration if exists
          if parser_tree and parser_tree.package:
            package_name = parser_tree.package.name
          else:
            package_name = None

          if (maxlen < len(token_vector)):
            maxlen = len(token_vector)

    for version, versionmap, versionlabel in zip(self.versions, self.mapdata, self.labeldata):
      token_matrix = []
      with open(str(versionmap), 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        reader.__next__()
        for line in reader:
          #get path_file of each file
          path_file =os.path.normpath((str(self.root) + line[0][27:-24]).replace("\\","/"))
          with open(path_file, encoding='cp1256') as file:
            src = file.read()
          token_vector = []
          parser_tree = None
          try:
            parser_tree = javalang.parse.parse(src)
            for path, node in parser_tree:
              if (str(type(node)) in class_selec):
                token_vector.append(node.name)
          except:
            pass

          # Get the package declaration if exists
          if parser_tree and parser_tree.package:
            package_name = parser_tree.package.name
          else:
            package_name = None

          # If source file has package declaration
          if package_name:
            src_id = (package_name + '.' +
                      os.path.basename(path_file))
          else:
            src_id = os.path.basename(path_file)
          Project[version].src_files[src_id] = SourceFile(path_file)
          token_matrix.append(token_vector)
      #change token_vector to inter_vector
      for src_id, token_vector in zip(Project[version].src_files,token_matrix):
        vectori = []
        for para in token_vector:
          vectori.append(vocab.index(para) + 1)
        for _ in range(maxlen - len(vectori)):
          vectori.append(0)
        Project[version].src_files[src_id].interVector = vectori
        # print(Project[version].src_files[src_id].interVector)

      # get Traditional Feature
      with open(str(versionlabel), 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        reader.__next__()
        for line in reader:
          src_id = line[2] + ".java"
          if (src_id in Project[version].src_files):
            Project[version].src_files[src_id].tradFeature=[float(i) for i in line[3:-1]]
            Project[version].src_files[src_id].label = 0 if (int(line[-1])==0) else 1
            Project[version].src_files[src_id].version = line[1]
          else:
            continue

    return Project

def test():
  import datasets

  parser = Parser(datasets.camel)
  t = parser.Parser()

  i = 0
  for src_id in t[1.4].src_files:
    print( src_id, t[1.4].src_files[src_id].tradFeature )
    i = i+1
    if i==3:
      break

if __name__ == "__main__":
  test()