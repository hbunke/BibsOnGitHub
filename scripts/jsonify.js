#!/usr/bin/env node

/*
 * Copyright 2018 Philipp Zumstein
 *
 * This software may be modified and distributed under the terms
 * of the MIT license. See the LICENSE file for details.
 */

var fs = require("fs")

function jsonifyList() {
  var data = fs.readFileSync('list.md');
  var lines = data.toString().split('\n\n');
  var subsection = 0;// counter for the subsections
  var ret = {
    org: [],
    people: []
  };
  for (let i=0; i<lines.length; i++) {
    if (lines[i].includes('---')) {
      subsection++;
    } else {
      let splitLine = lines[i].split("(https://github.com/");
      if (splitLine.length==2) {
        let label = splitLine[0].replace(/\[[^\]]*\]$/, '').trim();
        let githubName = splitLine[1].replace(/\)\s*$/, '');
        let object = {
          label: label,
          githubName: githubName
        };
        if (subsection==1) ret.org.push(object);
        if (subsection==2) {
          let labelSplit = object.label.split('(');
          if (labelSplit.length==2) {
            object.label = labelSplit[0].trim();
            object.affiliation = labelSplit[1].replace(/\)$/, '');
          }
          ret.people.push(object);
        }
      }
    }
  }
  return ret;
}

module.exports = {
  jsonifyList: jsonifyList
}

if (require.main === module) {
  console.log(JSON.stringify(jsonifyList(), null, 2));
}

