# Database

### Generalization

```
pigeon    sparrow   dove

            |
            |
            \/
            Birds

```

### Specialization

```
    Person
       |
       |
      ISA
      /  \
Student   Teacher
```

### Normalization
- `First normal form` - all the attributes in a relation must have atomic domains
- `Second normal form` - 
  Student_Project relation that the prime key   attributes are Stu_ID and Proj_ID. According to the rule, non-key attributes, i.e. Stu_Name and Proj_Name   must be dependent upon both and not on any of the   prime key attribute individually. But we find that   Stu_Name can be identified by Stu_ID and Proj_Name   can be identified by Proj_ID independently. This is   called partial dependency, which is not allowed in   Second Normal Form.
- `Third Normal Form` - 
  Student_detail relation, Stu_ID is the key and only prime key attribute. We find that City can be      identified by       Stu_ID as well as Zip itself. Neither Zip is a superkey nor is City a prime attribute. Additionally,    Stu_ID → Zip →       City, so there exists transitive dependency.

### Indexing
- `Primary Index` − Primary index is defined on an ordered data file. The data file is ordered on a key field. The key field is generally the primary key of the relation.

- `Secondary Index` − Secondary index may be generated from a field which is a candidate key and has a unique value in every record, or a non-key with duplicate values.

- `Clustering Index` − Clustering index is defined on an ordered data file. The data file is ordered on a non-key field.