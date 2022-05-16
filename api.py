from flask import Flask, render_template, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey 
api=Flask(__name__)
api.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:azertyuiop@localhost:5432/prbase'
api.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(api)

class Categories(db.Model):
   __tablename__='Categories'
   id = db.Column(db.Integer, primary_key=True)
   libelle_categorie = db.Column(db.String(10), nullable=False)
   livres=db.relationship('Livres', backref='Categories', lazy=True)
   def init(self,libelle_categorie):
        self.libelle_categorie=libelle_categorie
   
   def insert_categories(self):
           db.session.add(self)
           db.session.commit()

   def format_categories(self):
           return {
                "id":self.id,
                "libelle_categorie":self.libelle_categorie
           }
   
   def delete_categories(s):
        db.session.delete(s)
        db.session.commit()
   
   def update(s):
        db.session.commit()



class Livres(db.Model):
   __tablename__='Livres'
   id = db.Column(db.Integer, primary_key=True)
   isbn = db.Column(db.String(13), nullable=False)
   titre = db.Column(db.String(30), nullable=False)
   date_publication = db.Column(db.Date(), nullable=False)
   auteur = db.Column(db.String(30), nullable=False)
   editeur = db.Column(db.String(30), nullable=False)
   categorie_id=db.Column(db.Integer, db.ForeignKey('Categories.id'),nullable=False)
   def init(self,isbn,titre,date_publication,auteur,editeur,categorie_id):
        self.isbn=isbn
        self.titre=titre
        self.date_publication=date_publication
        self.auteur=auteur
        self.editeur=editeur
        self.categorie_id=categorie_id


   def insert_livres(self):
           db.session.add(self)
           db.session.commit()

   def format_livres(self):
           return {
                "id":self.id,
                "isbn":self.isbn,
                "titre":self.titre,
                "date-publication":self.date_publication,
                "auteur":self.auteur,
                "editeur":self.editeur,
                "categorie_id":self.categorie_id
           }
   
   def delete_livres(s):
        db.session.delete(s)
        db.session.commit()
   
   def update(s):
        db.session.commit()

db.create_all()

@api.route('/')
def index():
    return 'Hello flask'

########################################################################
#################              Afficher catégories
########################################################################
@api.route("/categorie", methods=['GET'])
def list_category():
       list_categorie = Categories.query.all()
       categories = [categories.format_categories() for categories in list_categorie]
       if list_categorie is None:
            abort(500)
       else:        
              return jsonify({
              'Success':True,
              'Liste ':categories,
              'Nombre Catégories':len(list_categorie)
              })

########################################################################
#################              Afficher une catégorie
########################################################################
@api.route('/categorie/<int:id>', methods=['GET'])
def select_categorie(id):
       categories = Categories.query.get(id)
       if categories is None:
              abort(404)
       else:
              return jsonify({
                     'success':True,
                     'Categorie':categories.format_categories()
              })

########################################################################
#############                 Ajouter une categorie
########################################################################
@api.route('/categorie', methods=['POST'])
def add_category():
#Récupérer les données envoyées en json
        body = request.get_json()

#Récupérer les infos
        new_libelle_categorie = body.get('libelle_categorie', None)
        categorie = Categories(
        libelle_categorie=new_libelle_categorie)
        categorie.insert_categories()

        categories = Categories.query.all()
        categories_js = [data.format_categories()
        for data in categories]

        return jsonify({
        'Success': True,
        'Categorie': categories_js,
        'Nombre Categorie': len(categories)
        })

##############################################################
#########             Modifier une categorie
##############################################################
@api.route("/categorie/<int:id>", methods=['PATCH'])
def modify_category(id):
      categorie=Categories.query.get(id)

      body=request.get_json()

      categorie.libelle_categorie = body.get('libelle_categorie')
      categorie.update()

      return jsonify({
         'Success':True,
         'Categories': categorie.format_categories()
      })

##################################################################
##################         Supprimer une categorie
##################################################################
@api.route('/categorie/<int:id>', methods=['DELETE'])
def delete_categories(id):
     categorie=Categories.query.get(id)
     categories = Categories.query.all()
     categorie.delete_categories()

     return jsonify({
         'Success':True,
         'Categorie': categorie.id,
         'Nombre Categorie': len(categories)
     })

########################################################################
#################                Afficher livres
########################################################################
@api.route('/livres', methods = ['GET'])
def show_livres():
       livres = Livres.query.order_by(Livres.id).all()
       livre_format = [livre.format_livres() for livre in livres]
       
       return jsonify({
        'Success':True,
        'Livres':livre_format,
        'Nombre livres':len(livres)       
       })

###################################################################
###################          Afficher un livre 
###################################################################
@api.route('/livres/<int:id>', methods = ['GET'])
def show_livre(id):
    livre=Livres.query.get(id)
    if livre is None:
           abort(404)
    else:
           return jsonify({
              'Success':True,
              'Livre':livre.format_livres()
              })

###################################################################
###################         Ajouter un livre
###################################################################
@api.route('/livres', methods=['POST'])
def add_livre():
#Récupérer les données envoyées en json
        body = request.get_json()

#Récupérer chaque infos
        new_isbn = body.get('isbn')
        new_titre = body.get('titre')
        new_date_publication = body.get('date_publication')
        new_auteur = body.get('auteur')
        new_editeur = body.get('editeur')
        new_categories_id= body.get('categories_id')

        categories= Categories.query.get(new_categories_id)
        if categories is None:
              abort(404)
        else:
       
              livre = Livres(isbn=new_isbn, titre = new_titre, date_publication = new_date_publication, 
                            auteur=new_auteur, editeur= new_editeur, categorie_id = new_categories_id)
              livre.insert_livres()

              return jsonify({
              "Success":True,
              "Livre": livre.id,
              "Nombre livre":len(Livres.query.all())    
              })

##############################################################
##################           Modifier un livre
##############################################################
@api.route('/livres/<int:id>', methods=['PATCH'])
def modify_livres(id):
#Récupurer chaque infos
    body = request.get_json()
    livre = Livres.query.get(id)
    if livre is None:
        abort(404)
    else:
        livre.isbn =body.get('isbn')
        livre.titre =body.get('titre')
        livre.date_publication =body.get('date_publication')
        livre.auteur =body.get('auteur')
        livre.editeur =body.get('editeur')
        livre.categorie_id =body.get('categorie_id')
        
        categorie = Categories.query.get(body.get('categorie_id'))
        if categorie is None:
               abort(404)
        livre.update()
        livres = Livres.query.all()
        return ({
            "success":True,
            "id livre": livre.id,
            "Liste de livres": [livre.format_livres() for livre in livres]            
        })

##################################################################
##################           Supprimer un livre
##################################################################
@api.route('/livres/<int:id>', methods=['DELETE'])
def delete_livre(id):
       livre = Livres.query.get(id)
       if livre is None:
              abort(404)
       livre.delete_livres()
       return jsonify({
              'Success':True,
              'id livre':livre.id,
              'Nombre livre':len(Livres.query.all())
       })

@api.errorhandler(404)
def page_not_found(e):
    return jsonify({
        "succes":False,
        "response":"Ressource not found",
    })


@api.errorhandler(400)
def page_not_found(e):
    return jsonify({
        "succes":False,
        "response":"Bad request",
    })


@api.errorhandler(405)
def page_not_found(e):
    return jsonify({
        "succes":False,
        "response":"Method not allowed",
    })

if __name__ == "__api__":
     api.run(debug = True)