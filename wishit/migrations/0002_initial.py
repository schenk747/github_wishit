# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'WishList'
        db.create_table(u'wishit_wishlist', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(related_name='wishlist_creator', to=orm['auth.User'])),
        ))
        db.send_create_signal(u'wishit', ['WishList'])

        # Adding M2M table for field viewers on 'WishList'
        m2m_table_name = db.shorten_name(u'wishit_wishlist_viewers')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('wishlist', models.ForeignKey(orm[u'wishit.wishlist'], null=False)),
            ('user', models.ForeignKey(orm[u'auth.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['wishlist_id', 'user_id'])

        # Adding model 'Gift'
        db.create_table(u'wishit_gift', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('text', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('wisher', self.gf('django.db.models.fields.related.ForeignKey')(related_name='gift_wisher', to=orm['auth.User'])),
            ('buyer', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='gift_buyer', null=True, to=orm['auth.User'])),
            ('reserver', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='gift_reserver', null=True, to=orm['auth.User'])),
            ('wish_list', self.gf('django.db.models.fields.related.ForeignKey')(related_name='gift_list', to=orm['wishit.WishList'])),
        ))
        db.send_create_signal(u'wishit', ['Gift'])


    def backwards(self, orm):
        # Deleting model 'WishList'
        db.delete_table(u'wishit_wishlist')

        # Removing M2M table for field viewers on 'WishList'
        db.delete_table(db.shorten_name(u'wishit_wishlist_viewers'))

        # Deleting model 'Gift'
        db.delete_table(u'wishit_gift')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'wishit.gift': {
            'Meta': {'object_name': 'Gift'},
            'buyer': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'gift_buyer'", 'null': 'True', 'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'reserver': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'gift_reserver'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'wish_list': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'gift_list'", 'to': u"orm['wishit.WishList']"}),
            'wisher': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'gift_wisher'", 'to': u"orm['auth.User']"})
        },
        u'wishit.wishlist': {
            'Meta': {'object_name': 'WishList'},
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'wishlist_creator'", 'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'viewers': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'wishlist_viewer'", 'symmetrical': 'False', 'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['wishit']