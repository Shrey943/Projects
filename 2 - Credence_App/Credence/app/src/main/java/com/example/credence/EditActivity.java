package com.example.credence;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ProgressBar;
import android.widget.TextView;

public class EditActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_edit);

        TextView beliefT = findViewById(R.id.belief2);
        TextView commentT = findViewById(R.id.comment2);
        TextView commentWord = findViewById(R.id.commentText);
        Button update = findViewById(R.id.update2);
        Button edit = findViewById(R.id.edit);

        final Intent intent = getIntent();

        final String ID = intent.getStringExtra("ID");
        final int id = Integer.parseInt(ID);

        final SharedPreferences shrd = getSharedPreferences("demo", MODE_PRIVATE);
        String belief = shrd.getString("belief"+id,"Belief");
        String comment = shrd.getString("comment"+id,"");
        final float per = shrd.getFloat("per"+id,(float)25.55);

        beliefT.setText(belief);
        if (comment.length()==0){
            commentWord.setAlpha(0);
            commentT.setAlpha(0);
            commentT.setClickable(false);
        }
        else{commentT.setText(comment);}
        ProgressBar progressBar = findViewById(R.id.progress_bar);
        TextView progressT = findViewById(R.id.progessText);

        progressBar.setProgress((int) per);
        progressT.setText(per+ " %");

        update.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent1 = new Intent(EditActivity.this, UpdateActivity.class);
                intent1.putExtra("ID",ID);
                startActivity(intent1);

            }
        });
        edit.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent1 = new Intent(EditActivity.this,EditActivity2.class);
                intent1.putExtra("ID",ID);
                startActivity(intent1);
            }
        });





    }
}